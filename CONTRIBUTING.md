# CONTRIBUTING

If you follow these contributing guidelines your patch will likely
make it into a release a little quicker.

## Contributing

1. Fork the repo.
2. Run the tests. We only take pull requests with passing tests, and
   it's great to know that you have a clean slate.
3. Add a test for your change. Only refactoring and documentation
   changes require no new tests. If you are adding functionality
   or fixing a bug, please add a test.
4. Make the test pass.
5. Add yourself to `./MAINTAINERS`.
6. Push to your fork and submit a pull request.

## Dependencies

This is a Python 3 project.

This project depends on the modules for
* BeautifulSoup
* Tix
* Tkinter

Testing this project depends on
* pyunit
* nose

By default the tests use a baseline version of Python.

It is recommended to use [virtualenv](https://docs.python-guide.org/dev/virtualenvs/)
 to install a personal copy of python just for this project.

Alternatively, [pipenv](https://docs.python-guide.org/dev/virtualenvs/)
 can be used if you just need the odd modules like Tix.

## Syntax and style

Pylint is recommended, particularly `python3-pylint` if available on your
platform.

### Automatically run the tests

See the files in `tests/*py`.

Run them with `make` using the `./Makefile` provided  This does not try to use
`virtualenv` or `pipenv`.

The makefile will try to use nose (or python3-nose).

## Integration tests

The unit tests just check the code runs, not that it does exactly what
we want on a real machine.

For end-to-end testing, start the application and interact with it directly.
