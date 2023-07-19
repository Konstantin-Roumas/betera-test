<h1>How to install and launch scripts</h1>
<p>First step: You need to clone <a href="https://github.com/Konstantin-Roumas/betera-test.git"> repository.</a></p>

`git clone https://github.com/Konstantin-Roumas/betera-test.git`

<p>Second step: You need install additional packages.</p>

`pip install -r requirements.txt`

<p>Third step: Launch database.py</p>

`python3 database.py`

<p>Fourth step: <b>betera.db</b> should be appear with two tables in it.</p>
<p>After that you can launch my solution on python and SQL*</p>

`python3 solution.py`

`sqlite3 betera.db < betera.sql`
<p>
* To run sql script from cli you should have sqlite3 package
<br>

Ubuntu/Ubuntu-based distros: 

`sudo apt install sqlite`

Arch/Arch-based distros:

`pacman -S sqlite`

Mac:

`brew install sqlite`

Fedora:

`sudo dnf install sqlite`

</p>