Summary:	A MIDI sound file player
Summary(de):	Zum Abspielen von midi-Dateien auf FM-, GUS- und MIDI-Geräten
Summary(fr):	Joue des fichiers midi sur des périphériques FM, GUS et MIDI
Summary(pl):	Odtwarzacz plików MIDI
Summary(tr):	FM, GUS ve MIDI aygýtlarý üzerindeki midi dosyalarýný çalar
Name:		playmidi
Version:	2.4
Release:	12
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.linpeople.org/pub/People/nathan/%{name}-%{version}.tar.gz
# Source0-md5: ce27bfbc4e122f103bf3d2fe8d253011
Patch0:		%{name}-hertz.patch
Patch1:		%{name}-make.patch
Patch2:		%{name}-midimap.patch
Patch3:		%{name}-glibconfig.patch
BuildRequires:	gtk+-devel
BuildRequires:	ncurses-devel >= 5.0
%ifarch %{ix86} alpha
BuildRequires:	svgalib-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/midi
%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

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
Summary:	An X Window System based MIDI sound file player
Summary(de):	X-Window-Schnittstelle für den MIDI-Soundplayer
Summary(pl):	Odtwarzacz plików MIDI dla systemu X Window
Summary(tr):	MIDI ses çalýcý için X arayüzü
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}

%description X11
Playmidi-X11 provides an X Window System interface for playing MIDI
(Musical Instrument Digital Interface) sound files through a sound
card synthesizer. Install playmidi-X11 if you want to use an X
interface to play MIDI sound files using your computer's sound card.

%description X11 -l de
X-Programm zum Abspielen von MIDI-Sounddateien über einen Soundkarten-
Synthesizer. Enthält einfache Schlagzeug-Samples für einfache
FM-Synthesizers.

%description X11 -l fr
Programme X pour jouer des fichiers MIDI par le synthétiseur d'une
carte son. Il contient des exemples de batterie de base pour les
synthétiseurs FM simples.

%description X11 -l pl
Playmidi-X11 dostarcza interfejs opary o system X Window umo¿liwiaj±cy
odtwarzanie plików MIDI poprzez kartê d¼wiêkow±.

%description X11 -l tr
MIDI ses dosyalarýný çalan playmidi uygulamasýnýn X arayüzü.

%package svga
Summary:	An SVGAlib based MIDI sound file player
Summary(pl):	Odtwarzacz plików MIDI wykorzystuj±cy SVGAlib
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description svga
Playmidi-svga provides an SVGAlib interface for playing MIDI (Musical
Instrument Digital Interface) sound files through a sound card
synthesizer. Install playmidi-svga if you want to use an SVGAlib
interface to play MIDI sound files using your computer's sound card.

%description svga -l pl
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
%{__make} playmidi xplaymidi \
%ifarch %{ix86} alpha
	splaymidi \
%endif
	OPT_FLAGS="%{rpmcflags}" <<EOF
2
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_mandir}/man1,%{_bindir},%{_appdefsdir}}

install playmidi xplaymidi $RPM_BUILD_ROOT%{_bindir}
install XPlaymidi.ad $RPM_BUILD_ROOT%{_appdefsdir}/XPlaymidi
install std.o3 drums.o3 std.sb drums.sb $RPM_BUILD_ROOT%{_sysconfdir}
install playmidi.1 $RPM_BUILD_ROOT%{_mandir}/man1

%ifarch %{ix86} alpha
install splaymidi $RPM_BUILD_ROOT%{_bindir}
echo '.so playmidi.1' > $RPM_BUILD_ROOT%{_mandir}/man1/splaymidi.1
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS QuickStart
%attr(755,root,root) %{_bindir}/playmidi
%dir %{_sysconfdir}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/std.o3
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/std.sb
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/drums.o3
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/drums.sb
%{_mandir}/man1/playmidi.1*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xplaymidi
%{_appdefsdir}/XPlaymidi

%ifarch %{ix86} alpha
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/splaymidi
%{_mandir}/man1/splaymidi.1*
%endif
