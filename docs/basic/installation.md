

# Installation

Telethon is a Python library, which means you need to download and install
Python from https://www.python.org/downloads/ if you haven't already. Once
you have Python installed, run:

```sh
pip3 install -U telethon --user
```

To install or upgrade the library to the latest version.

## Installing Development Versions

If you want the *latest* unreleased changes,
you can run the following command instead:

```
pip3 install -U https://github.com/LonamiWebs/Telethon/archive/master.zip --user
```

!!! Note

    The development version may have bugs and is not recommended for production
    use. However, when you are [reporting a library bug](https://github.com/LonamiWebs/Telethon/issues/), you should try if the
    bug still occurs in this version.

## Verification

To verify that the library is installed correctly, run the following command:

```sh
python3 -c "import telethon; print(telethon.__version__)"
```

The version number of the library should show in the output.


## Optional Dependencies

If [cryptg] is installed, **the library will work a lot faster**, since
encryption and decryption will be made in C instead of Python. If your
code deals with a lot of updates or you are downloading/uploading a lot
of files, you will notice a considerable speed-up (from a hundred kilobytes
per second to several megabytes per second, if your connection allows it).
If it's not installed, [pyaes] will be used (which is pure Python, so it's
much slower).

If [pillow] is installed, large images will be automatically resized when
sending photos to prevent Telegram from failing with "invalid image".
Official clients also do this.

If [aiohttp] is installed, the library will be able to download
[WebDocument](https://tl.telethon.dev/?q=WebDocument) media files (otherwise
you will get an error).

If [hachoir] is installed, it will be used to extract metadata from files
when sending documents. Telegram uses this information to show the song's
performer, artist, title, duration, and for videos too (including size).
Otherwise, they will default to empty values, and you can set the attributes
manually.

!!! Note

    Some of the modules may require additional dependencies before being
    installed through ``pip``. If you have an ``apt``-based system, consider
    installing the most commonly missing dependencies:

    ```sh
    apt update
    apt install clang lib{jpeg-turbo,webp}-dev python{,-dev} zlib-dev
    pip install -U --user setuptools
    pip install -U --user telethon cryptg pillow
    ```

    Thanks to [@bb010g] for writing down this nice list.

[cryptg]: https://github.com/cher-nov/cryptg
[pyaes]: https://github.com/ricmoo/pyaes
[pillow]: https://python-pillow.org
[aiohttp]: https://docs.aiohttp.org
[hachoir]: https://hachoir.readthedocs.io
[@bb010g]: https://static.bb010g.com
