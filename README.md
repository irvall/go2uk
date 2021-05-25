# go2uk
UK's traffic light system in your command line. For tracking current corona restrictions when travelling to United Kingdom.
Creates a local DB file that by default only rewrites itself after a day or six hours of recent fetch.

## Setup

Get the required dependencies by typing:

```bash
➤ pip install -r requirements.txt
```

## Usage

Type either the country you want information on, a color (red, amber, green), or nothing (shows the full list):

```bash
➤ go2uk denmark
(retrieved data from log at 2021-05-25 11:21:47.033104)
Denmark: amber
```
or color:
```bash
➤ go2uk green
(retrieved data from log at 2021-05-25 11:21:47.033104)
Green (12 countries):
* Australia
* Brunei
* Falkland Islands
* Faroe Islands
* Gibraltar
* Iceland
* Israel and Jerusalem
* New Zealand
* Portugal (including the Azores and Madeira)
* Singapore
* South Georgia and South Sandwich Islands
* St Helena, Ascension and Tristan da Cunha
```
or no arguments:
```bash
➤ go2uk
(retrieved data from log at 2021-05-25 11:21:47.033104)
Red (43 countries):
* Angola
* Argentina
...

Amber (173 countries):
* Afghanistan
* Akrotiri and Dhekelia
...

Green (12 countries):
* Australia
* Brunei
...
```
