Summary:	A MIDI sound file player
Summary(de):	Zum Abspielen von midi-Dateien auf FM-, GUS- und MIDI-Geräten
Summary(fr):	Joue des fichiers midi sur des périphériques FM, GUS et MIDI
Summary(pl):	Odtwarzacz plików MIDI
Summary(tr):	FM, GUS ve MIDI aygýtlarý üzerindeki midi dosyalarýný çalar
Name:		playmidi
Version:	2.4
Release:	9
License:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source:		ftp://ftp.linpeople.org/pub/People/nathan/%{name}-%{version}.tar.gz
Patch0:		playmidi-hertz.patch
Patch1:		playmidi-make.patch
Patch2:		playmidi-midimap.patch
Patch3:		playmidi-glibconfig.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	XFree86-devel
%ifarch %ix86
BuildRequires:	svgalib
%endif
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_sysconfdir	/etc/midi

%description
Playmidi plays MIDI (Musicial Instrument Digital Interface) sound files
through a sound card synthesizer. This package includes basic drum samples
for use with simple FM synthesizers. Install playmidi if you want to play
MIDI files using your computer's sound card.

%description -l de
Spielt MIDI-Sounddateien über einen Soundkarten-Synthesizer ab. Enthält
einfache Schlagzeug-Samples für einfache FM-Synthesizer.

%description -l fr
Programme X pour jouer des fichiers MIDI par le synthétiseur d'une carte
son. Il contient des exemples de batterie de base pour les synthétiseurs FM
simples.

%description -l pl
Playmidi odtwarza pliki MIDI poprzez syntetyzer karty d¼wiêkowej. Pakiet
zawiera podstawowe instrumenty perkusyjne do wykorzystania z prostymi
syntetyzerami FM.

%description -l tr
Bir ses kartýnýn ses birleþtiricisi aracýlýðýyla MIDI ses dosyalarýný çalar.
FM ses birleþtirici ile kullaným için ana davul sesi örneklerý içerir.

%package X11
Summary:	An X Window System based MIDI sound file player.
Summary(de):	X-Windows-Schnittstelle für den MIDI-Soundplayer
Summary(pl):	Odtwarzacz plików MIDI dla systemu X Window
Summary(tr):	MIDI ses çalýcý için X arayüzü
Group:		Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}

%description X11
Playmidi-X11 provides an X Window System interface for playing MIDI
(Musical Instrument Digital Interface) sound files through a sound card
synthesizer. Install playmidi-X11 if you want to use an X interface to
play MIDI sound files using your computer's sound card.

%description -l de X11
X-Programm zum Abspielen von MIDI-Sounddateien über einen Soundkarten-
Synthesizer. Enthält einfache Schlagzeug-Samples für einfache
FM-Synthesizers.

%description -l fr X11
Programme X pour jouer des fichiers MIDI par le synthétiseur d'une carte
son. Il contient des exemples de batterie de base pour les synthétiseurs FM
simples.

%description -l pl X11
Playmidi-X11 dostarcza interfejs opary o system X Window umo¿liwiaj±cy
odtwarzanie plików MIDI poprzez kartê d¼wiêkow±.

%description -l tr X11
MIDI ses dosyalarýný çalan playmidi uygulamasýnýn X arayüzü.

%package svga
Summary:	An SVGAlib based MIDI sound file player.
Summary(pl):	Odtwarzacz plików MIDI wykorzystuj±cy SVGAlib.
Group:		Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}

%description svga
Playmidi-svga provides an SVGAlib interface for playing MIDI (Musical
Instrument Digital Interface) sound files through a sound card synthesizer.
Install playmidi-svga if you want to use an SVGAlib interface to play MIDI
sound files using your computer's sound card.

%description -l pl svga
Playmidi-svga dostarcza interfejs oparty o SVGAlib umo¿liwiaj±cy
odtwarzanie plików MIDI poprzez kartê d¼wiêkow±.

%prep
%setup -q
# awe_voice.h is now part of the kernel source.
rm awe_voice.h
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
#PATH=.:$PATH

%ifarch %ix86
make playmidi splaymidi xplaymidi <<EOF
2
EOF
%else
make playmidi xplaymidi <<EOF
2
EOF
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT{%{_bindir},/usr/X11R6/{bin,lib/X11/app-defaults}}

install -s playmidi $RPM_BUILD_ROOT%{_bindir}
install -s xplaymidi $RPM_BUILD_ROOT/usr/X11R6/bin
install XPlaymidi.ad $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/XPlaymidi

%ifarch %ix86
install -s splaymidi $RPM_BUILD_ROOT%{_bindir}
%endif

install playmidi.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo ".so playmidi.1" > $RPM_BUILD_ROOT%{_mandir}/man1/splaymidi.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/*\
	BUGS QuickStart

install -d $RPM_BUILD_ROOT%{_sysconfdir}
install std.o3 drums.o3 std.sb drums.sb $RPM_BUILD_ROOT%{_sysconfdir}

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
%config /usr/X11R6/lib/X11/app-defaults/XPlaymidi
%attr(755,root,root) /usr/X11R6/bin/xplaymidi

%ifarch %ix86

%files svga
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/splaymidi
%{_mandir}/man1/splaymidi.1*

%endif
