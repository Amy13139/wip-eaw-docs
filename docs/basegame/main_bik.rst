.. _basegame-filetype-bik:

*********
BIK Files
*********


.. _basegame-filetype-dat-about:

About
=====
All .BIK files in EaW and FoC are movie files of the proprietary `Bink Video Format <https://wikipedia.org/wiki/Bink_Video>`_.
The format was reverse-engineered and added to the `FFmpeg Utility`_ under the libavcodec. All .BIK files
are given an internal ID through an :ref:`XML File <basegame-filetype-xml>` of the
:doc:`BinkMovies XML Type <xml/auto/binkmovie>`.


.. _basegame-filetype-dat-struct:

Usage
=====


Viewing
-------
Bink movies can be viewed by any media player that has or can use the libavcodec. This includes many common media
players, such as `VLC Media Player <https://www.videolan.org>`_.


Conversion
----------
The easiest way to convert a Bink Video is to use the previously mentioned `FFmpeg Utility`_, which can
both encode and decode most video and audio formats.


.. _FFmpeg Utility: ffmpeg.org


.. _basegame-filetype-dat-import:

EaW-Godot Port Connection
=========================
An importer for Godot would be difficult to implement, but BIK files can be easily converted to a compatible format (see
the above conversion section).
