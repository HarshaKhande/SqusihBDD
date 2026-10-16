# -*- coding: UTF-8 -*-

@OnFeatureStart
def feature_start(context):
    test.log("BDD Feature Start", context.title)
    testSettings.logScreenshotOnFail = True
    testSettings.logScreenshotOnError = True

@OnScenarioStart
def scenario_start(context):
    test.log("BDD Scenario Start", context.title)
    context.userData = {}

@OnStepStart
def step_start(context):
    test.log("BDD Step", context.text)

@OnScenarioEnd
def scenario_end(context):
    test.log("BDD Scenario End", context.title)
