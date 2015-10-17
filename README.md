# Vietcong1.eu

[![Build Status](https://travis-ci.org/garncarz/vietcong1.eu.svg?branch=master)](https://travis-ci.org/garncarz/vietcong1.eu)
[![Coverage Status](https://coveralls.io/repos/garncarz/vietcong1.eu/badge.svg?branch=master&service=github)](https://coveralls.io/github/garncarz/vietcong1.eu?branch=master)

## Installation

Needed: [Python 3](https://www.python.org/)

1. `git clone https://github.com/garncarz/vietcong1.eu.git`
2. `virtualenv3 virtualenv`
3. Make sure `virtualenv/bin` is in `PATH`.
4. `cd vietcong1.eu`
5. `pip install -r requirements.txt`
6. Create `vietcong/settings/local.py`, it should begin with `from .base import *`, settings override and specifications should follow. Or you can just `from .development import *` if you're developing.


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


## Demo

`./manage.py demo` fills DB with randomly generated content.


## Testing

`./manage.py test`

With coverage: `coverage run --source='.' ./manage.py test`, then `coverage report` or `coverage html`.
