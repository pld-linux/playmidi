Summary:	A MIDI sound file player
Summary(de):	Zum Abspielen von midi-Dateien auf FM-, GUS- und MIDI-Geräten
Summary(fr):	Joue des fichiers midi sur des périphériques FM, GUS et MIDI
Summary(pl):	Odtwarzacz plików MIDI
Summary(tr):	FM, GUS ve MIDI aygýtlarý üzerindeki midi dosyalarýný çalar
Name:		playmidi
Version:	2.4
Release:	11
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Source0:	ftp://ftp.linpeople.org/pub/People/nathan/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-hertz.patch
Patch1:		%{name}-make.patch
Patch2:		%{name}-midimap.patch
Patch3:		%{name}-glibconfig.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	gtk+-devel
%ifarch %ix86
BuildRequires:	svgalib-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/midi
%define		_xbindir	/usr/X11R6/bin

%description
Playmidi plays MIDI (Musicial Instrument Digital Interface) sound
files through a sound card synthesizer. This package includes basic
drum samples for use with simple FM synthesizers. Install playmidi if
you want to play MIDI files using your computer's sound card.

%description -l de
Spielt MIDI-Sounddateien über einen Soundkarten-Synthesizer ab.
Enthält einfache Schlagzeug-Samples für einfache FM-Synthesizer.

%description -l fr
Programme X pour jouer des fichiers MIDI par le synthétiseur d'une
carte son. Il contient des exemples de batterie de base pour les
synthétiseurs FM simples.

%description -l pl
Playmidi odtwarza pliki MIDI poprzez syntetyzer karty d¼wiêkowej.
Pakiet zawiera podstawowe instrumenty perkusyjne do wykorzystania z
prostymi syntetyzerami FM.

%description -l tr
Bir ses kartýnýn ses birleþtiricisi aracýlýðýyla MIDI ses dosyalarýný
çalar. FM ses birleþtirici ile kullaným için ana davul sesi örneklerý
içerir.

%package X11
Summary:	An X Window System based MIDI sound file player.
Summary(de):	X-Windows-Schnittstelle für den MIDI-Soundplayer
Summary(pl):	Odtwarzacz plików MIDI dla systemu X Window
Summary(tr):	MIDI ses çalýcý için X arayüzü
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}

%description X11
Playmidi-X11 provides an X Window System interface for playing MIDI
(Musical Instrument Digital Interface) sound files through a sound
card synthesizer. Install playmidi-X11 if you want to use an X
interface to play MIDI sound files using your computer's sound card.

%description -l de X11
X-Programm zum Abspielen von MIDI-Sounddateien über einen Soundkarten-
Synthesizer. Enthält einfache Schlagzeug-Samples für einfache
FM-Synthesizers.

%description -l fr X11
Programme X pour jouer des fichiers MIDI par le synthétiseur d'une
carte son. Il contient des exemples de batterie de base pour les
synthétiseurs FM simples.

%description -l pl X11
Playmidi-X11 dostarcza interfejs opary o system X Window umo¿liwiaj±cy
odtwarzanie plików MIDI poprzez kartê d¼wiêkow±.

%description -l tr X11
MIDI ses dosyalarýný çalan playmidi uygulamasýnýn X arayüzü.

%package svga
Summary:	An SVGAlib based MIDI sound file player
Summary(pl):	Odtwarzacz plików MIDI wykorzystuj±cy SVGAlib
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Requires:	%{name} = %{version}

%description svga
Playmidi-svga provides an SVGAlib interface for playing MIDI (Musical
Instrument Digital Interface) sound files through a sound card
synthesizer. Install playmidi-svga if you want to use an SVGAlib
interface to play MIDI sound files using your computer's sound card.

%description -l pl svga
Playmidi-svga dostarcza interfejs oparty o SVGAlib umo¿liwiaj±cy
odtwarzanie plików MIDI poprzez kartê d¼wiêkow±.

%prep
%setup -q
# awe_voice.h is now part of the kernel source.
rm -f awe_voice.h
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
#PATH=.:$PATH

%ifarch %ix86
%{__make} OPT_FLAGS="%{rpmcflags}" playmidi splaymidi xplaymidi <<EOF
2
EOF
%else
%{__make} OPT_FLAGS="%{rpmcflags}" playmidi xplaymidi <<EOF
2
EOF
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_mandir}/man1,%{_sysconfdir}} \
	$RPM_BUILD_ROOT{%{_bindir},%{_prefix}/X11R6/{bin,lib/X11/app-defaults}} \
	$RPM_BUILD_ROOT%{_applnkdir}/Multimedia

%{__install} playmidi $RPM_BUILD_ROOT%{_bindir}
%{__install} xplaymidi $RPM_BUILD_ROOT%{_xbindir}
%{__install} XPlaymidi.ad $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/app-defaults/XPlaymidi
%{__install} std.o3 drums.o3 std.sb drums.sb $RPM_BUILD_ROOT%{_sysconfdir}
%{__install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

%ifarch %ix86
%{__install} splaymidi $RPM_BUILD_ROOT%{_bindir}
%endif

%{__install} playmidi.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo ".so playmidi.1" > $RPM_BUILD_ROOT%{_mandir}/man1/splaymidi.1

gzip -9nf BUGS QuickStart

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/playmidi
%dir %{_sysconfdir}
%config %{_sysconfdir}/std.o3
%config %{_sysconfdir}/std.sb
%config %{_sysconfdir}/drums.o3
%config %{_sysconfdir}/drums.sb
%{_mandir}/man1/playmidi.1*

%files X11
%defattr(644,root,root,755)
%config %{_prefix}/X11R6/lib/X11/app-defaults/XPlaymidi
%attr(755,root,root) %{_xbindir}/xplaymidi
%{_applnkdir}/Multimedia/*

%ifarch %ix86
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/splaymidi
%{_mandir}/man1/splaymidi.1*
%endif
