#!/usr/bin/env casperjs
/**
 * Created by guangtouling on 16/5/30.
 */
//实例化casper模块
var casper = require('casper').create();
//初始化词典
var dic= {'#url-field':''};
//从命令行参数中获取值
dic['#url-field'] = casper.cli.args[0];

//程序入口;打开首页,并检测是否成功
casper.start('http://freeget.co/',function(){
    //检查是否有input标签,判断是否正常进入主页
    if(this.exists('input')){
        //this.echo('打开主页成功!');
         //this.capture("1.png");
        //截图,看是否成功输入
        //点击解析按钮
    }
    else {
        //this.capture("1.png");
        this.warn('打开主页失败').exit();
    }
});

//从输入框输入
casper.then(function(){
    this.fillSelectors('#url-input',dic);
    this.capture('2.png');
});

//点击解析按钮
casper.then(function(){
    this.click('#extract-button');
});

//等待1s,然后截图
casper.wait(1500,function(){
    if (this.exists('a[url^="/"]')){
        //this.echo('可以提取');
        //this.capture('3.png');
    }
    else{
        this.capture('3.png');
        this.warn('视频已删除或者未更新').exit();
        }
});

//点击提取
casper.then(function(){
    this.click('#video-download-button');
})

//等待1.5秒后,输出网页源码
casper.wait(1500,function(){
    //this.capture('4.png');
    this.echo(this.getHTML());
});
//casper.exit()
//这一句至关重要,没有它程序不会运行
casper.run();
