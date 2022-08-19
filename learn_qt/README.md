# Qt for Python -- Building GUI apps

Due to my current job, I have to develop a GUI so my optimiz app could be more user friendly. A co-worker suggested this env, because it seems a lil' modern compared to TK\_inter -- an env I experienced with almost 1 yr ago --.

![The result](hello_work.png)

## Qt Installation

	$ pip install pyside6

Is not necessary to download the online installer that Qt recommends. If you do so, you must create a user account in order to install.

Test installation:<br>
<code>
import PySide6.QtCore

#print PySide6 version
print(PySide6.__version__)

#print Qt version
print(PySide6.QtCore.__version__)
</code>

## Issue found in my environment

*qt_graph.py* When trying to bind qt with matplotlib an [issue](https://github.com/ndlopez/learn_python/issues/1) was found. I couldnt fix it in spite of searching for a solution in DuckDuckGo.

## Running Environment

- OS: MacOS 10.15
- Editor: Emacs
- Python Libraries
	- Python3.8
	- numpy 1.19.1
	- scipy 1.5.2
	- Matplotlib 3.3.1
	- PySide6 v6.3.1
