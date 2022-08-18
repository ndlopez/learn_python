# Qt for Python -- Building GUI apps

I didnt know that it was kinda easy to build GUI apps. I decided to give it a try in Qt.
![The result](hello_work.png)
## Qt Installation

	$ pip install pyside6

Is not necessary to download the online installer that Qt recommends. User Id is needed to install.

Test installation:<br>
<code>
import PySide6.QtCore

#print PySide6 version
print(PySide6.__version__)

#print Qt version
print(PySide6.QtCore.__version__)
</code>
