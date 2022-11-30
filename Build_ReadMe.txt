1、安装MSYS2环境，然后修改根目录的 msys2_shell.cmd 里面的 set MSYS2_PATH_TYPE=inherit，去掉这行的注释，保证能够在msys2中找到vs提供的开发套件。
2、打开“x86 Native Tools Command Prompt for VS 2019” ，启动 msys2_shell.cmd -mingw32,32位;
	或者打开 “x64 Native Tools Command Prompt for VS 2019” 启动 或者 msys2_shell.cmd -mingw64 64位
3、下载zlib与源码然后编译，参考链接：https://ffmpeg.org/platform.html#Microsoft-Visual-C_002b_002b-or-Intel-C_002b_002b-Compiler-for-Windows
	找到宿主的lib目录，在msys2中通过找 echo %LIB%，然后将zlib.h和zlibconf.h复制到include里面，将zlib.lib复制到lib中
	Notes:
	If you wish to build with zlib support, you will have to grab a compatible zlib binary from somewhere, with an MSVC import lib, or if you wish to link statically, you can follow the instructions below to build a compatible zlib.lib with MSVC. Regardless of which method you use, you must still follow step 3, or compilation will fail.
	Grab the zlib sources.
	Edit win32/Makefile.msc so that it uses -MT instead of -MD, since this is how FFmpeg is built as well.
	Edit zconf.h and remove its inclusion of unistd.h. This gets erroneously included when building FFmpeg.
	Run nmake -f win32/Makefile.msc.
	Move zlib.lib, zconf.h, and zlib.h to somewhere MSVC can see.
	FFmpeg has been tested with the following on i686 and x86_64:
	Visual Studio 2013 Pro and Express
	Intel Composer XE 2013
	Intel Composer XE 2013 SP1
	Anything else is not officially supported.
	
4、执行 build_ffmpeg_msvc.sh 或者 build_ffmpeg_msvc.sh release

5、然后执行根目录的main.py复制产物。



