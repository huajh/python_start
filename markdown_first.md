[toc]


## exanmple of markdown


###  homepage 
[huajh7.com](http://huajh7.com)


### quotes


> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
> 
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.
> 
> machine
> >  This is nested blockquote.
> 
>  Back to the first level.
> return shell_exec("echo $input | $markdown_script");

### pargraphs 
* Red
+ Bule
	* machine
- good
1. Bird
2. parish

~~strik through~~

`import tempfile; print(tempfile.gettempdir())`

==hightlight==

-----------------------------------------



### codes 

`python`

```python
class ReqStrSugRepr(type):

    def __init__(cls, name, bases, attrd):
        super(ReqStrSugRepr, cls).__init__(name, bases, attrd)

        if '__str__' not in attrd:
            raise TypeError("Class requires overriding of __str__()")

        if '__repr__' not in attrd:
            warn(
                'Class suggets overrding of __repr__()\n',
                stacklevel=3)
```



质能方程公式：$E=mc^2$

$$\min_{x,y} \sum_{i=1}^{N} (x_i+ 10 + y_i)^2 $$



### 脚注（footnote）

实现方式如下:

比如PHP[^1] Markdown Extra [^2] 是这样的。

[^1]: Markdown是一种纯文本标记语言

[^2]: 开源笔记平台，支持Markdown和笔记直接发为博文


### 引用方式：
I get 10 times more traffic from [Google][1] than from [Yahoo][2] or [MSN][3].  


### 下划线

---下划线---

### Images 

#### 内联方式：

![lenaNoise](./image_denoising/lenaNoise.jpg "lenaNoise")


#### 引用方式：
![alt text][id] 

[id]: ./PoissonImageEditing/mona-leber-final.jpg "mona-leber"


![]()



[1]: http://google.com/        "Google" 
[2]: http://search.yahoo.com/  "Yahoo Search" 
[3]: http://search.msn.com/    "MSN Search"


  


  


  


  


  


  


  


  


  


  


  




 







