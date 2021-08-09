%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -d -s

%define date 20210809

Summary:	An abstract SDL soundfile decoder
Name:		SDL2_sound
Version:	2.0.0
Release:	%{?date:0.%{date}.}1
Group:		Sound
License:	LGPLv2+
URL:		http://www.icculus.org/SDL_sound
# 
Source0:	https://github.com/icculus/SDL_sound/archive/refs/heads/main.tar.gz
# There seem to be 2 different versions of SDL detection cmake
# files -- upstream assumes they set SDL2_LIBRARIES and SDL2_INCLUDE_DIRS
# while the version we have sets SDL2_LIBRARY and SDL2_INCLUDE_DIR
# Let's support both variants...
Patch0:		https://github.com/icculus/SDL_sound/pull/23.patch
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(flac)
BuildRequires:	libmikmod-devel
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(speex)
BuildRequires:	physfs-devel
BuildRequires:	doxygen

%description
SDL_sound is a library that handles the decoding of several popular
sound file formats, such as .WAV and .MP3. It is meant to make the
programmer's sound playback tasks simpler. The programmer gives
SDL_sound a filename, or feeds it data directly from one of many
sources, and then reads the decoded waveform data back at her
leisure. If resource constraints are a concern, SDL_sound can process
sound data in programmer-specified blocks. Alternately, SDL_sound can
decode a whole sound file and hand back a single pointer to the whole
waveform. SDL_sound can also handle sample rate, audio format, and
channel conversion on-the-fly and behind-the-scenes, if the programmer
desires.


%package -n %{libname}
Summary:	SDL graphics drawing primitives and other support functions
Group:		System/Libraries

%description -n %{libname}
SDL_sound is a library that handles the decoding of several popular
sound file formats, such as .WAV and .MP3. It is meant to make the
programmer's sound playback tasks simpler. The programmer gives
SDL_sound a filename, or feeds it data directly from one of many
sources, and then reads the decoded waveform data back at her
leisure. If resource constraints are a concern, SDL_sound can process
sound data in programmer-specified blocks. Alternately, SDL_sound can
decode a whole sound file and hand back a single pointer to the whole
waveform. SDL_sound can also handle sample rate, audio format, and
channel conversion on-the-fly and behind-the-scenes, if the programmer
desires.

%package -n %{develname}
Summary:	Header files and more to develop SDL_sound applications
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Header files and more to develop SDL_sound applications.

%package -n %{staticname}
Summary:	Static SDL_sound libraries
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}

%description -n %{staticname}
Static SDL_sound libraries.

%prep
%autosetup -p1 -n SDL_sound-main
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libSDL2_sound.so.%{major}*

%files -n %{develname}
%{_libdir}/lib*.so
%{_includedir}/SDL2/*

%files -n %{staticname}
%{_libdir}/lib*.a
