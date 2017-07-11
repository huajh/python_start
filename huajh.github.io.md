### install software
create repository: `huajh7.github.io`
install `node.js`

### install hexo 

`$ npm install -g hexo-cli`

`$ hexo`

### bulid the hexo blog
```
// 建立一个博客文件夹，并初始化博客，<folder>为文件夹的名称，可以随便起名字
$ hexo init <folder>
// 进入博客文件夹，<folder>为文件夹的名称
$ cd <folder>
// node.js的命令，根据博客既定的dependencies配置安装所有的依赖包
$ npm install
```


### edit _config.yml

```
title: huajh7
subtitle: homepage
description: 
author: Junhao Hua
language: zh-CN
timezone: Asia/Shanghai
```

`url: http://huajh7.com`


```yml
deploy:
  type: git
  repo: https://github.com/huajh/huajh.github.io.git
  branch: master
```

`hexo g` or `hexo generate`

`hexo server`



clone the repo in /huajh7.github.io

`hexo clean`

`hexo generate`

`hexo deploy`
