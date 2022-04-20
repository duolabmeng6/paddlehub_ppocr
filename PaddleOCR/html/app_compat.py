# coding:utf-8
# Copyright (c) 2020  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import traceback
import time

from flask import Flask, request

from paddlehub.serving.model_service.base_model_service import cv_module_info
from paddlehub.serving.model_service.base_model_service import nlp_module_info
from paddlehub.serving.model_service.base_model_service import v2_module_info
from paddlehub.utils import utils, log

filename = 'HubServing-%s.log' % time.strftime("%Y_%m_%d", time.localtime())


def package_result(status: str, msg: str, data: dict):
    '''
    Package message of response.

    Args:
         status(str): Error code
            ========   ==============================================================================================
            Code       Meaning
            --------   ----------------------------------------------------------------------------------------------
            '000'      Return results normally
            '101'      An error occurred in the predicting method
            '111'      Module is not available
            '112'      Use outdated and abandoned HTTP protocol format
            ========   ===============================================================================================
         msg(str): Detailed info for error
         data(dict): Result of predict api.

    Returns:
        dict: Message of response

    Examples:
        .. code-block:: python

            data = {'result': 0.002}
            package_result(status='000', msg='', data=data)
    '''
    return {"status": status, "msg": msg, "results": data}


def predict_v2(module_info: dict, input: dict):
    '''

    Predict with `serving` API of module.

    Args:
         module_info(dict): Module info include module name, method name and
                            other info.
         input(dict): Data to input to predict API.

    Returns:
        dict: Response after packaging by func `package_result`

    Examples:
        .. code-block:: python

            module_info = {'module_name': 'lac'}}
            data = {'text': ['今天天气很好']}
            predict_v2(module_info=module_info, input=data)
    '''
    serving_method_name = module_info["method_name"]
    serving_method = getattr(module_info["module"], serving_method_name)
    predict_args = module_info["predict_args"].copy()
    predict_args.update(input)

    for item in serving_method.__code__.co_varnames:
        if item in module_info.keys():
            predict_args.update({item: module_info[item]})
    try:
        output = serving_method(**predict_args)
    except Exception as err:
        log.logger.error(traceback.format_exc())
        return package_result("101", str(err), "")

    return package_result("000", "", output)


def create_app(init_flag: bool = False, configs: dict = None):
    '''
    Start one flask instance and ready for HTTP requests.

    Args:
         init_flag(bool): Whether the instance need to be initialized with
                          `configs` or not
         configs(dict): Module configs for initializing.

    Returns:
        One flask instance.

    Examples:
        .. code-block:: python

            create_app(init_flag=False, configs=None)
    '''
    if init_flag is False:
        if configs is None:
            raise RuntimeError("Lack of necessary configs.")
        config_with_file(configs)

    app_instance = Flask(__name__)
    app_instance.config["JSON_AS_ASCII"] = False
    app_instance.logger = log.get_file_logger(filename)

    @app_instance.route("/", methods=["GET", "POST"])
    def index():
        '''
        Provide index page.
        '''
        return open('/PaddleOCR/html/index.html').read()

        return '暂不提供可视化界面，请直接使用脚本进行请求。<br/>No visual ' \
               'interface is provided for the time being, please use the' \
               ' python script to make a request directly.'

    @app_instance.before_request
    def before_request():
        '''
        Add id info to `request.data` before request.
        '''
        request.data = {"id": utils.md5(request.remote_addr + str(time.time()))}

    @app_instance.route("/predict/<module_name>", methods=["POST"])
    def predict_serving_v2(module_name: str):
        '''
        Http api for predicting.

        Args:
            module_name(str): Module name for predicting.

        Returns:
            Result of predicting after packaging.
        '''
        if module_name in v2_module_info.modules:
            module_info = v2_module_info.get_module_info(module_name)
        else:
            msg = "Module {} is not available.".format(module_name)
            return package_result("111", msg, "")
        inputs = request.json
        if inputs is None:
            results = "This usage is out of date, please use 'application/json' as content-type to post to /predict/%s. See 'https://github.com/PaddlePaddle/PaddleHub/blob/release/v1.6/docs/tutorial/serving.md' for more details." % (
                module_name)
            return package_result("112", results, "")

        results = predict_v2(module_info, inputs)
        return results

    return app_instance


def config_with_file(configs: dict):
    '''
    Config `cv_module_info` and `nlp_module_info` by configs.

    Args:
        configs(dict): Module info and configs

    Examples:
        .. code-block:: python

            configs = {'lac': {'version': 1.0.0, 'category': nlp}}
            config_with_file(configs=configs)
    '''
    for key, value in configs.items():
        if "CV" == value["category"]:
            cv_module_info.add_module(key, {key: value})
        elif "NLP" == value["category"]:
            nlp_module_info.add_module(key, {key: value})
        v2_module_info.add_module(key, {key: value})
        logger = log.get_file_logger(filename)
        logger.info("%s==%s" % (key, value["version"]))


def run(configs: dict = None, port: int = 8866):
    '''
    Run flask instance for PaddleHub-Serving

    Args:
         configs(dict): module info and configs
         port(int): the port of the webserver

    Examples:
        .. code-block:: python

            configs = {'lac': {'version': 1.0.0, 'category': nlp}}
            run(configs=configs, port=8866)
    '''
    logger = log.get_file_logger(filename)
    if configs is not None:
        config_with_file(configs)
    else:
        logger.error("Start failed cause of missing configuration.")
        return
    my_app = create_app(init_flag=True)
    my_app.run(host="0.0.0.0", port=port, debug=False, threaded=False)
    log.logger.info("PaddleHub-Serving has been stopped.")
