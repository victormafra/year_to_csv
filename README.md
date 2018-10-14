# Year to CSV

A simple python script to translate your [Year in Pixels](https://play.google.com/store/apps/details?id=ar.teovogel.yip) to a `.csv` file.

## Table of Contents

* [Environment](#environment)
* [Development](#development)
* [Example](#example)

## Environment

* [Python 3.6.6](https://www.python.org)
* [pipenv](https://docs.pipenv.org)

```sh
pip install pipenv
```

## Development

Install dependencies:

```sh
pipenv install
```

Run:

```sh
pipenv run python converter.py year_in_pixels.jpg YYYY
```

## Example

To generate the image from the app, first make sure your `FIRST MONTH` is set to January on the `CONFIG` tab. Then just press the share button on the upper right corner and the image will be automatically saved on your `Pictures` folder.

Consider the following exported image:

![Example Exported Image](example.jpg?raw=true "Example Exported Image")

By Running:

```sh
pipenv run python converter.py example.jpg 2018
```

You get a `.csv` like this:

| Date,Color   |
|--------------|
| 2018-01-01,5 |
| 2018-01-02,3 |
| 2018-01-03,2 |
| 2018-01-04,5 |
| 2018-01-05,4 |
| 2018-01-06,3 |
| 2018-01-07,4 |
| 2018-01-08,1 |
| 2018-01-09,2 |
| 2018-01-10,5 |
| 2018-01-11,4 |
| 2018-01-12,4 |
| 2018-01-13,3 |
| 2018-01-14,5 |
| 2018-01-15,3 |
| 2018-01-16,2 |
| 2018-01-17,3 |
| 2018-01-18,5 |
| 2018-01-19,5 |
| 2018-01-20,3 |
| 2018-01-21,4 |
| 2018-01-22,2 |
| 2018-01-23,1 |
| 2018-01-24,4 |
| 2018-01-25,5 |
| 2018-01-26,2 |
| 2018-01-27,5 |
| 2018-01-28,4 |
| 2018-01-29,1 |
| 2018-01-30,4 |
| 2018-01-31,2 |
| 2018-02-01,4 |
| 2018-02-02,3 |
| 2018-02-03,4 |
| 2018-02-04,1 |
| 2018-02-05,2 |
| 2018-02-06,5 |
| 2018-02-07,1 |
| 2018-02-08,4 |
| 2018-02-09,3 |
| 2018-02-10,2 |
| 2018-02-11,4 |
| 2018-02-12,2 |
| 2018-02-13,3 |
| 2018-02-14,5 |
| 2018-02-15,3 |
| 2018-02-16,2 |
| 2018-02-17,0 |
| 2018-02-18,5 |
| 2018-02-19,0 |
| 2018-02-20,0 |
| 2018-02-21,4 |
| 2018-02-22,3 |
| 2018-02-23,1 |
| 2018-02-24,4 |
| 2018-02-25,5 |
| 2018-02-26,3 |
| 2018-02-27,1 |
| 2018-02-28,2 |
| 2018-03-01,4 |
| 2018-03-02,5 |
| 2018-03-03,1 |
| 2018-03-04,2 |
| 2018-03-05,4 |
| 2018-03-06,5 |
| 2018-03-07,2 |
| 2018-03-08,5 |
| 2018-03-09,3 |
| 2018-03-10,4 |
| 2018-03-11,1 |
| 2018-03-12,3 |
| 2018-03-13,0 |
| 2018-03-14,4 |
| 2018-03-15,0 |
| 2018-03-16,2 |
| 2018-03-17,0 |
| 2018-03-18,4 |
| 2018-03-19,0 |
| 2018-03-20,0 |
| 2018-03-21,4 |
| 2018-03-22,4 |
| 2018-03-23,3 |
| 2018-03-24,4 |
| 2018-03-25,2 |
| 2018-03-26,4 |
| 2018-03-27,4 |
| 2018-03-28,5 |
| 2018-03-29,3 |
| 2018-03-30,5 |
| 2018-03-31,1 |
| 2018-04-01,2 |
| 2018-04-02,4 |
| 2018-04-03,4 |
| 2018-04-04,1 |
| 2018-04-05,1 |
| 2018-04-06,5 |
| 2018-04-07,0 |
| 2018-04-08,3 |
| 2018-04-09,4 |
| 2018-04-10,5 |
| 2018-04-11,1 |
| 2018-04-12,5 |
| 2018-04-13,3 |
| 2018-04-14,2 |
| 2018-04-15,4 |
| 2018-04-16,5 |
| 2018-04-17,4 |
| 2018-04-18,5 |
| 2018-04-19,1 |
| 2018-04-20,3 |
| 2018-04-21,1 |
| 2018-04-22,3 |
| 2018-04-23,2 |
| 2018-04-24,4 |
| 2018-04-25,1 |
| 2018-04-26,4 |
| 2018-04-27,2 |
| 2018-04-28,5 |
| 2018-04-29,1 |
| 2018-04-30,2 |
| 2018-05-01,5 |
| 2018-05-02,3 |
| 2018-05-03,4 |
| 2018-05-04,2 |
| 2018-05-05,5 |
| 2018-05-06,4 |
| 2018-05-07,5 |
| 2018-05-08,4 |
| 2018-05-09,2 |
| 2018-05-10,1 |
| 2018-05-11,4 |
| 2018-05-12,2 |
| 2018-05-13,5 |
| 2018-05-14,3 |
| 2018-05-15,2 |
| 2018-05-16,1 |
| 2018-05-17,4 |
| 2018-05-18,5 |
| 2018-05-19,4 |
| 2018-05-20,3 |
| 2018-05-21,2 |
| 2018-05-22,1 |
| 2018-05-23,5 |
| 2018-05-24,4 |
| 2018-05-25,2 |
| 2018-05-26,4 |
| 2018-05-27,2 |
| 2018-05-28,5 |
| 2018-05-29,3 |
| 2018-05-30,1 |
| 2018-05-31,2 |
| 2018-06-01,1 |
| 2018-06-02,5 |
| 2018-06-03,2 |
| 2018-06-04,5 |
| 2018-06-05,4 |
| 2018-06-06,3 |
| 2018-06-07,2 |
| 2018-06-08,4 |
| 2018-06-09,2 |
| 2018-06-10,4 |
| 2018-06-11,4 |
| 2018-06-12,3 |
| 2018-06-13,1 |
| 2018-06-14,5 |
| 2018-06-15,4 |
| 2018-06-16,4 |
| 2018-06-17,3 |
| 2018-06-18,2 |
| 2018-06-19,1 |
| 2018-06-20,5 |
| 2018-06-21,2 |
| 2018-06-22,4 |
| 2018-06-23,2 |
| 2018-06-24,1 |
| 2018-06-25,5 |
| 2018-06-26,2 |
| 2018-06-27,4 |
| 2018-06-28,3 |
| 2018-06-29,2 |
| 2018-06-30,5 |
| 2018-07-01,0 |
| 2018-07-02,3 |
| 2018-07-03,0 |
| 2018-07-04,1 |
| 2018-07-05,1 |
| 2018-07-06,2 |
| 2018-07-07,3 |
| 2018-07-08,0 |
| 2018-07-09,5 |
| 2018-07-10,0 |
| 2018-07-11,2 |
| 2018-07-12,3 |
| 2018-07-13,4 |
| 2018-07-14,3 |
| 2018-07-15,5 |
| 2018-07-16,2 |
| 2018-07-17,4 |
| 2018-07-18,0 |
| 2018-07-19,0 |
| 2018-07-20,0 |
| 2018-07-21,4 |
| 2018-07-22,4 |
| 2018-07-23,5 |
| 2018-07-24,3 |
| 2018-07-25,5 |
| 2018-07-26,4 |
| 2018-07-27,1 |
| 2018-07-28,2 |
| 2018-07-29,5 |
| 2018-07-30,3 |
| 2018-07-31,4 |
| 2018-08-01,1 |
| 2018-08-02,4 |
| 2018-08-03,3 |
| 2018-08-04,0 |
| 2018-08-05,5 |
| 2018-08-06,5 |
| 2018-08-07,4 |
| 2018-08-08,1 |
| 2018-08-09,0 |
| 2018-08-10,2 |
| 2018-08-11,3 |
| 2018-08-12,4 |
| 2018-08-13,3 |
| 2018-08-14,3 |
| 2018-08-15,4 |
| 2018-08-16,2 |
| 2018-08-17,1 |
| 2018-08-18,2 |
| 2018-08-19,0 |
| 2018-08-20,4 |
| 2018-08-21,0 |
| 2018-08-22,5 |
| 2018-08-23,5 |
| 2018-08-24,4 |
| 2018-08-25,5 |
| 2018-08-26,1 |
| 2018-08-27,2 |
| 2018-08-28,3 |
| 2018-08-29,1 |
| 2018-08-30,5 |
| 2018-08-31,5 |
| 2018-09-01,0 |
| 2018-09-02,1 |
| 2018-09-03,3 |
| 2018-09-04,2 |
| 2018-09-05,4 |
| 2018-09-06,5 |
| 2018-09-07,1 |
| 2018-09-08,2 |
| 2018-09-09,5 |
| 2018-09-10,4 |
| 2018-09-11,3 |
| 2018-09-12,2 |
| 2018-09-13,2 |
| 2018-09-14,3 |
| 2018-09-15,2 |
| 2018-09-16,1 |
| 2018-09-17,2 |
| 2018-09-18,4 |
| 2018-09-19,2 |
| 2018-09-20,3 |
| 2018-09-21,2 |
| 2018-09-22,1 |
| 2018-09-23,4 |
| 2018-09-24,3 |
| 2018-09-25,2 |
| 2018-09-26,5 |
| 2018-09-27,3 |
| 2018-09-28,5 |
| 2018-09-29,1 |
| 2018-09-30,4 |
| 2018-10-01,5 |
| 2018-10-02,2 |
| 2018-10-03,3 |
| 2018-10-04,4 |
| 2018-10-05,2 |
| 2018-10-06,1 |
| 2018-10-07,2 |
| 2018-10-08,1 |
| 2018-10-09,3 |
| 2018-10-10,3 |
| 2018-10-11,1 |
| 2018-10-12,4 |
| 2018-10-13,5 |
| 2018-10-14,0 |
| 2018-10-15,0 |
| 2018-10-16,0 |
| 2018-10-17,4 |
| 2018-10-18,2 |
| 2018-10-19,3 |
| 2018-10-20,5 |
| 2018-10-21,0 |
| 2018-10-22,2 |
| 2018-10-23,3 |
| 2018-10-24,5 |
| 2018-10-25,3 |
| 2018-10-26,3 |
| 2018-10-27,2 |
| 2018-10-28,3 |
| 2018-10-29,2 |
| 2018-10-30,4 |
| 2018-10-31,5 |
| 2018-11-01,3 |
| 2018-11-02,4 |
| 2018-11-03,4 |
| 2018-11-04,3 |
| 2018-11-05,4 |
| 2018-11-06,3 |
| 2018-11-07,2 |
| 2018-11-08,3 |
| 2018-11-09,4 |
| 2018-11-10,2 |
| 2018-11-11,3 |
| 2018-11-12,4 |
| 2018-11-13,2 |
| 2018-11-14,1 |
| 2018-11-15,3 |
| 2018-11-16,0 |
| 2018-11-17,0 |
| 2018-11-18,4 |
| 2018-11-19,4 |
| 2018-11-20,5 |
| 2018-11-21,2 |
| 2018-11-22,3 |
| 2018-11-23,4 |
| 2018-11-24,5 |
| 2018-11-25,4 |
| 2018-11-26,4 |
| 2018-11-27,4 |
| 2018-11-28,3 |
| 2018-11-29,5 |
| 2018-11-30,4 |
| 2018-12-01,5 |
| 2018-12-02,2 |
| 2018-12-03,4 |
| 2018-12-04,2 |
| 2018-12-05,3 |
| 2018-12-06,5 |
| 2018-12-07,2 |
| 2018-12-08,3 |
| 2018-12-09,5 |
| 2018-12-10,3 |
| 2018-12-11,4 |
| 2018-12-12,3 |
| 2018-12-13,4 |
| 2018-12-14,3 |
| 2018-12-15,2 |
| 2018-12-16,0 |
| 2018-12-17,4 |
| 2018-12-18,2 |
| 2018-12-19,3 |
| 2018-12-20,4 |
| 2018-12-21,4 |
| 2018-12-22,3 |
| 2018-12-23,2 |
| 2018-12-24,3 |
| 2018-12-25,2 |
| 2018-12-26,1 |
| 2018-12-27,3 |
| 2018-12-28,4 |
| 2018-12-29,4 |
| 2018-12-30,4 |
| 2018-12-31,5 |
