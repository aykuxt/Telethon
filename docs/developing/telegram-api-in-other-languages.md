# Telegram API in Other Languages

Telethon was made for **Python**, and as far as I know, there is no
*exact* port to other languages. However, there *are* other
implementations made by awesome people (one needs to be awesome to
understand the official Telegram documentation) on several languages
(even more Python too), listed below:

## C

Possibly the most well-known unofficial open source implementation out
there by [@vysheng](https://github.com/vysheng),
[tgl](https://github.com/vysheng/tgl), and its console client
[telegram-cli](https://github.com/vysheng/tg). Latest development
has been moved to [BitBucket](https://bitbucket.org/vysheng/tdcli).

## C++

The newest (and official) library, written from scratch, is called
[tdlib](https://github.com/tdlib/td) and is what the Telegram X
uses. You can find more information in the official documentation,
published [here](https://core.telegram.org/tdlib/docs/).

## JavaScript

[Ali Gasymov](https://github.com/alik0211) made the
[@mtproto/core](https://github.com/alik0211/mtproto-core) library for the
browser and nodejs installable via [npm](https://www.npmjs.com/package/@mtproto/core).

[painor](https://github.com/painor) is the primary author of 
[gramjs](https://github.com/gram-js/gramjs), a Telegram client implementation in JavaScript.

## Kotlin

[Kotlogram](https://github.com/badoualy/kotlogram) is a Telegram
implementation written in Kotlin (one of the
[official](https://blog.jetbrains.com/kotlin/2017/05/kotlin-on-android-now-official/)
languages for [Android](https://developer.android.com/kotlin/index.html)) by
[@badoualy](https://github.com/badoualy), currently as a beta – yet working.

## Language-Agnostic

[Taas](https://www.t-a-a-s.ru/) is a service that lets you use Telegram API with any
HTTP client via API. Using tdlib under the hood, Taas is commercial service, but allows
free access if you use under 5000 requests per month.

## PHP

A PHP implementation is also available thanks to
[@danog](https://github.com/danog) and his
[MadelineProto](https://github.com/danog/MadelineProto) project, with a very
nice [online documentation](https://daniil.it/MadelineProto/API_docs/) too.

## Python

A fairly new (as of the end of 2017) Telegram library written from the
ground up in Python by
[@delivrance](https://github.com/delivrance) and his
[Pyrogram](https://github.com/pyrogram/pyrogram) library.
There isn't really a reason to pick it over Telethon and it'd be kinda
sad to see you go, but it would be nice to know what you miss from each
other library in either one so both can improve.

## Rust

The [grammers](https://github.com/Lonami/grammers) library is made by
the [same author as Telethon's](https://github.com/Lonami)! If you are
looking for a Telethon alternative written in Rust, this is a valid option!

Another older, work-in-progress implementation, on Rust is made by
[@JuanPotato](https://github.com/JuanPotato) under the fancy
name of [Vail](https://github.com/JuanPotato/Vail).
