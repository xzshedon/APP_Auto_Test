# encoding: utf-8

''' html报告相关 '''

titles = '自动化回归测试'


def header(titles):
    header = '''<!DOCTYPE html>
        <html>
        <head>
            <title>%s</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <!-- 引入 Bootstrap -->
            <link href="https://cdn.bootcss.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
            <!-- HTML5 Shim 和 Respond.js 用于让 IE8 支持 HTML5元素和媒体查询 -->
            <!-- 注意： 如果通过 file://  引入 Respond.js 文件，则该文件无法起效果 -->
            <!--[if lt IE 9]>
             <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
             <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
            <![endif]-->
            <style type="text/css">
                .hidden-detail,.hidden-tr{
                    display:none;
                }
            </style>
        </head>
        <body>
        ''' % titles
    return header


connent = '''<div  class='col-md-4 col-md-offset-4' style='margin-left:3%;'><h1>回归用例测试结果</h1>'''


def index(starttime, endtime, pass_num, fail_num):
    test_info = '''
        <table  class="table table-hover table-condensed">
            <tbody>
                <tr>
    		    <td><strong>开始时间:</strong> %s</td></tr>
    		    <td><strong>结束时间:</strong> %s</td></tr>
    		    <td><strong>耗时:</strong> %s</td></tr>
    		    <td><strong>结果:</strong><span >Pass: <strong >%s</strong> Fail: <strong >%s</strong></span></td>                  
    		    </tr> 
    		</tbody>
    	</table>
    	</div> ''' % (starttime, endtime, (endtime - starttime), pass_num, fail_num)
    return test_info


test_result = '''<div class="row " style="margin:60px">
        <div style='margin-top: 18%;' >
        <div class="btn-group" role="group" aria-label="...">
            <button type="button" id="check-all" class="btn btn-primary">所有用例</button>
            <button type="button" id="check-success" class="btn btn-success">成功用例</button>
            <button type="button" id="check-danger" class="btn btn-danger">失败用例</button>
        </div>
        <div class="btn-group" role="group" aria-label="...">
        </div>
        <table class="table table-hover table-condensed table-bordered" style="word-wrap:break-word; word-break:break-all; margin-top: 7px;">
		<tr >
            <td><strong>测试设备</strong></td>
            <td><strong>用例编号</strong></td>
            <td><strong>所属模块</strong></td>
            <td><strong>参数</strong></td>
            <td><strong>预期</strong></td>
            <td><strong>结果</strong></td>
            <td><strong>截图</strong></td>
        </tr>
    '''


def pass_fail(result):
    if result == 'pass':
        result_color = '''<td bgcolor="green">pass</td>'''
    else:
        result_color = '''<td bgcolor="red">fail</td>'''
    return result_color


def details(device, id, model, parm, asserts, result, pic):
    test_details = '''
            <tr class="case-tr %s">
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                %s
                <td><img src='%s' width='150px',height='150px'></td>
            </tr>
        ''' % (device, device, id, model, parm, asserts, pass_fail(result), pic)
    return test_details


bottom = '''</div></div></table><script src="https://code.jquery.com/jquery.js"></script>
            <script src="https://cdn.bootcss.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
            <script type="text/javascript">
                $("#check-danger").click(function(e){
                    $(".case-tr").removeClass("hidden-tr");
                    $(".success").addClass("hidden-tr");
                    $(".warning").addClass("hidden-tr");
                    $(".error").addClass("hidden-tr");
                });
                $("#check-warning").click(function(e){
                     $(".case-tr").removeClass("hidden-tr");
                    $(".success").addClass("hidden-tr");
                    $(".danger").addClass("hidden-tr");
                    $(".error").addClass("hidden-tr");
                });
                $("#check-success").click(function(e){
                     $(".case-tr").removeClass("hidden-tr");
                    $(".warning").addClass("hidden-tr");
                    $(".danger").addClass("hidden-tr");
                    $(".error").addClass("hidden-tr");
                });
                $("#check-except").click(function(e){
                     $(".case-tr").removeClass("hidden-tr");
                    $(".warning").addClass("hidden-tr");
                    $(".danger").addClass("hidden-tr");
                    $(".success").addClass("hidden-tr");
                });
                $("#check-all").click(function(e){
                    $(".case-tr").removeClass("hidden-tr");
                });
            </script>
            </body></html>'''


def report(titles, starttime, endtime, pass_num, fail_num, id:list, devices:list,
           model:list, parm:list, asserts:list, relust:list, pic:list):
    rep =' '
    for i in range(len(devices)):
            if relust[i] == "pass":
                clazz = "success"
            else:
                clazz='error'
            rep += (details(devices[i], id[i], model[i], parm[i], asserts[i], clazz, pic[i]))
    text = header(titles)+connent+index(starttime, endtime, pass_num, fail_num)+test_result+rep+bottom
    return text


def create_html(filepath, titles, starttime, endtime, passge,fail, id:list, sheibei:list,
               model:list, parm:list, asserts:list, relusts:list, pic:list):
    texts = report(titles,starttime,endtime,passge,fail,id,sheibei,model,parm,asserts,relusts,pic)
    with open(filepath,'wb') as f:
        f.write(texts.encode('utf-8'))