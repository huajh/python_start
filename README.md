# just for learning python

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
 
 
> machine
> this is **rednerd as bold text**

 
`python`

```python
import tempfile; print(tempfile.gettempdir())
```

        
> hello world!


*machine learning*

* git add README.md
* git commit -m 'something'
* git puch origin master
* done!

`python`

```python
    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string
        __slots__ = ('fo','bar')
```

`java`

```java
public hello{
    public void sayhello()
    {
        System.out.println("hi, hello world!")
    }
}
```

`c`

```c

int main()
{
    print("hello world!")
}
```

