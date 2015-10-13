## Installation

Needed: [Python 3](https://www.python.org/)

1. `git clone https://github.com/garncarz/vietcong1.eu.git`
2. `virtualenv3 virtualenv`
3. Make sure `virtualenv/bin` is in `PATH`.
4. `cd vietcong1.eu`
5. `pip install -r requirements.txt`


### Installation of front-end

Needed: [npm](https://www.npmjs.com/), [Sass](http://sass-lang.com/)

Run:

```bash
$ cd front_end
$ npm install
$ node_modules/.bin/bower install
$ node_modules/.bin/grunt
```


## Run

Needed:

- `./manage.py migrate` for synchronizing the database schema.
- `./manage.py compilemessages` for compiling translations ([gettext](https://www.gnu.org/software/gettext/) needed).

Run:

`./manage.py runserver` when developing.
