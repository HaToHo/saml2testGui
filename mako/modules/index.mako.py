# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1385122658.868161
_enable_loop = True
_template_filename = 'mako/htdocs/index.mako'
_template_uri = 'index.mako'
_source_encoding = 'utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n\n<toaster-container toaster-options="{\'time-out\': 3000}"></toaster-container>\n\n<div ng-controller="IndexCtrl" >\n    <div class="container">\n        <div id="formContainer" class="jumbotron">\n\n            Tree layout:\n            <br>\n            <select ng-model="selectedItem"\n                ng-options="item.type for item in items" ng-change="updateTree();">\n            </select>\n\n            <br>\n\n            Available configurations:\n            <select id="targetIdp">\n                <option ng-repeat="tests in configList | orderBy:\'Name\':true">\n                     {{tests.Name}}\n                </option>\n            </select>\n\n            <br>\n\n            <!-- The information box -->\n            <div class="informationBox">\n                <div class="row" id="no-hover">\n\n                  <div class="col-xs-12 col-md-9">In the table bellow all tests are presented. Test which depend on others are makred with a little black arrow. In order to see the sub tests press the row containing an arrow. Tests could be executed at three levels, first of a single test could be executed. Then a test and it\'s sub tests could be executed by pressing the button "Run test". Last of all tests could be executed by pressing the button "Run all tests". The result of the tests are presented by color encoding the row containing the test and a written status. In order to get a more detailed version of the test result press the button "Show result"</div>\n\n                    <div class="col-xs-12 col-md-3">\n                        <div class="colorExampleBox" id="totalStatusINFORMATION">\n                            INFORMATION\n                        </div>\n\n                        <div class="colorExampleBox" id="totalStatusOK">\n                            OK\n                        </div>\n\n                        <div class="colorExampleBox" id="totalStatusWARNING">\n                            WARNING\n                        </div>\n\n                        <div class="colorExampleBox" id="totalStatusINTERACTION">\n                            INTERACTION\n                        </div>\n\n                        <div class="colorExampleBox" id="totalStatusERROR">\n                            ERROR\n                        </div>\n\n                        <div class="colorExampleBox" id="totalStatusCRITICAL">\n                            CRITICAL\n                        </div>\n                  </div>\n                </div>\n            </div>\n\n            <br>\n\n            <!-- The headline of the test table -->\n            <div class="col-lg-7" id="testHeadline">\n                Test\n            </div>\n\n            <div class="col-lg-1" id="testHeadline">\n                Status\n            </div>\n\n           <!-- Export button -->\n            <div class="col-lg-2" id="testHeadline">\n                <div class="btn-group">\n                    <button type="button" class="btn btn-primary btn-sm dropdown-toggle" data-toggle="dropdown">\n                        Export\n                        <span class="caret"></span>\n                    </button>\n                    <ul class="dropdown-menu">\n                        <li ng-click="exportTestResultToTextFile();"><a>Export result to excel file</a></li>\n                        <li ng-click="exportTestResultToExcel();"><a>Export result to text file</a></li>\n                    </ul>\n                </div>\n            </div>\n\n            <!-- Run all tests button-->\n            <div class="col-lg-2" id="testHeadline">\n                <button class="btn btn-primary" ng-click="runAllTest();">Run all tests</button>\n            </div>\n\n            <br>\n\n            <!-- The code which genertaes the rows of the test table -->\n            <div ng-repeat="data in currentFlattenedTree" class="row">\n\n                <div ng-show="data.visible == true" id="testRow">\n\n                    <div class="col-lg-7" id="totalStatus{{data.status}}" ng-click="showOrHideTests(data.testid);">\n                        <div id="level{{data.level}}">\n\n                            <span class="glyphicon glyphicon-info-sign" rel="tooltip" title="{{data.descr}}" id="infoIcon"></span>\n\n                            <img src="static/pitures/arrowRight.png" ng-show="data.hasChildren == true">\n\n                            <span ng-click="removeTestResult(data.testid);" rel="tooltip" title="{{data.descr}}">{{data.id}}</span>\n\n                        </div>\n                    </div>\n\n                    <div class="col-lg-1" id="totalStatus{{data.status}}">\n                        {{data.status}}\n                     </div>\n\n\n                    <div class="col-lg-2" id="totalStatus{{data.status}}">\n                        <button class="btn btn-default btn-xs" ng-click="showOrHideResult(data.testid);">Show result</button>\n                    </div>\n\n\n                    <div class="col-lg-2" id="totalStatus{{data.status}}">\n\n                        <div class="btn-group">\n                            <button class="btn btn-primary btn-sm dropdown-toggle" data-toggle="dropdown" id="runButton">\n                                Run test\n                                <span class="caret"></span>\n                            </button>\n                            <ul class="dropdown-menu">\n                                <li ng-click="runMultipleTest(data.id, data.testid);"><a>Run test and sub tests</a></li>\n                                <li ng-click="runOneTest(data.id, data.testid, true);"><a>Run this test only</a></li>\n                            </ul>\n                        </div>\n\n                    </div>\n\n                    <br>\n\n                    <div class="resultFrame" ng-show="data.showResult == true">\n                        Result:\n                        <br>\n\n                        <div ng-repeat="test in data.result">{{test}}</div>\n\n                    </div>\n\n                </div>\n\n            </div>\n\n            <div>\n                Test summary for last executed test: <p>Successful tests:{{resultSummary.success}}</p> <p>Failed tests:{{resultSummary.failed}}</p>\n            </div>\n\n        </div>\n    </div>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


