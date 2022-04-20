async function preInit(inputObj) {
    console.log("项目帮助 https://github.com/duolabmeng6/paddlehub_ppocr")
}

async function postInit(inputObj) {
    console.log("进入项目 输入 s deploy 部署项目 出现 domain 即可为api识别的api地址")
    console.log("例如: http://asc.ccc.xxxx.cn-shenzhen.fc.devsapp.net/predict/ocr_system")
}

module.exports = {
    postInit,
    preInit
}
