#!/usr/bin/env bash

set -e

source .env

s config add --AccessKeyID "$AccessKeyID" --AccessKeySecret "$AccessKeySecret" --AccountID "$AccountID" --aliasName "$aliasName"

s deploy