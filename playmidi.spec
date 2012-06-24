#
# TODO: port gtkplaymidi to GTK+ 1.2 (or better 2.x)
#
# Conditional build:
%bcond_with	gtk	# build gtkplaymidi program (not ready for GTK+ > 1.1)
%bcond_without	svga	# don't build splaymidi program
#
Summary:	A MIDI sound file player
Summary(de.UTF-8):   Zum Abspielen von midi-Dateien auf FM-, GUS- und MIDI-Geräten
Summary(fr.UTF-8):   Joue des fichiers midi sur des périphériques FM, GUS et MIDI
Summary(pl.UTF-8):   Odtwarzacz plików MIDI
Summary(tr.UTF-8):   FM, GUS ve MIDI aygıtları üzerindeki midi dosyalarını çalar
Name:		playmidi
Version:	2.5
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/playmidi/%{name}-%{version}.tar.gz
# Source0-md5:	ce27bfbc4e122f103bf3d2fe8d253011
Patch0:		%{name}-hertz.patch
Patch1:		%{name}-make.patch
Patch2:		%{name}-midimap.patch
URL:		http://sourceforge.net/projects/playmidi/
BuildRequires:	glib-devel >= 1.2
%{?with_gtk:BuildRequires:	gtk+-devel >= 1.2}
BuildRequires:	ncurses-devel >= 5.0
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/midi
%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
Playmidi plays MIDI (Musicial Instrument Digital Interface) sound
files through a sound card synthesizer. This package includes basic
drum samples for use with simple FM synthesizers. Install playmidi if
you want to play MIDI files using your computer's sound card.

%description -l de.UTF-8
Spielt MIDI-Sounddateien über einen Soundkarten-Synthesizer ab.
Enthält einfache Schlagzeug-Samples für einfache FM-Synthesizer.

%description -l fr.UTF-8
Programme X pour jouer des fichiers MIDI par le synthétiseur d'une
carte son. Il contient des exemples de batterie de base pour les
synthétiseurs FM simples.

%description -l pl.UTF-8
Playmidi odtwarza pliki MIDI poprzez syntetyzer karty dźwiękowej.
Pakiet zawiera podstawowe instrumenty perkusyjne do wykorzystania z
prostymi syntetyzerami FM.

%description -l tr.UTF-8
Bir ses kartının ses birleştiricisi aracılığıyla MIDI ses dosyalarını
çalar. FM ses birleştirici ile kullanım için ana davul sesi örneklerı
içerir.

%package X11
Summary:	An X Window System based MIDI sound file player
Summary(de.UTF-8):   X-Window-Schnittstelle für den MIDI-Soundplayer
Summary(pl.UTF-8):   Odtwarzacz plików MIDI dla systemu X Window
Summary(tr.UTF-8):   MIDI ses çalıcı için X arayüzü
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description X11
playmidi-X11 provides an X Window System interface for playing MIDI
(Musical Instrument Digital Interface) sound files through a sound
card synthesizer. Install playmidi-X11 if you want to use an X
interface to play MIDI sound files using your computer's sound card.

%description X11 -l de.UTF-8
X-Programm zum Abspielen von MIDI-Sounddateien über einen Soundkarten-
Synthesizer. Enthält einfache Schlagzeug-Samples für einfache
FM-Synthesizers.

%description X11 -l fr.UTF-8
Programme X pour jouer des fichiers MIDI par le synthétiseur d'une
carte son. Il contient des exemples de batterie de base pour les
synthétiseurs FM simples.

%description X11 -l pl.UTF-8
playmidi-X11 dostarcza oparty o X Window System interfejs
umożliwiający odtwarzanie plików MIDI poprzez kartę dźwiękową.

%description X11 -l tr.UTF-8
MIDI ses dosyalarını çalan playmidi uygulamasının X arayüzü.

%package gtk
Summary:	An GTK+ based MIDI sound file player
Summary(de.UTF-8):   GTK+-Schnittstelle für den MIDI-Soundplayer
Summary(pl.UTF-8):   Odtwarzacz plików MIDI oparty na GTK+
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description gtk
playmidi-gtk provides an GTK+-based interface for playing MIDI
(Musical Instrument Digital Interface) sound files through a sound
card synthesizer. Install playmidi-X11 if you want to use an X
interface to play MIDI sound files using your computer's sound card.

%description gtk -l de.UTF-8
GTK+-Programm zum Abspielen von MIDI-Sounddateien über einen
Soundkarten-Synthesizer. Enthält einfache Schlagzeug-Samples für
einfache FM-Synthesizers.

%description gtk -l fr.UTF-8
Programme GTK+ pour jouer des fichiers MIDI par le synthétiseur d'une
carte son. Il contient des exemples de batterie de base pour les
synthétiseurs FM simples.

%description gtk -l pl.UTF-8
playmidi-GTK+ dostarcza oparty na GTK+ interfejs umożliwiający
odtwarzanie plików MIDI poprzez kartę dźwiękową.

%package svga
Summary:	An SVGAlib based MIDI sound file player
Summary(pl.UTF-8):   Odtwarzacz plików MIDI wykorzystujący SVGAlib
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description svga
playmidi-svga provides an SVGAlib interface for playing MIDI (Musical
Instrument Digital Interface) sound files through a sound card
synthesizer. Install playmidi-svga if you want to use an SVGAlib
interface to play MIDI sound files using your computer's sound card.

%description svga -l pl.UTF-8
playmidi-svga dostarcza interfejs oparty o SVGAlib umożliwiający
odtwarzanie plików MIDI poprzez kartę dźwiękową.

%prep
%setup -q -n %{name}-2.4
# awe_voice.h is now part of the kernel source.
rm -f awe_voice.h
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} playmidi xplaymidi %{?with_gtk:gtkplaymidi} %{?with_svga:splaymidi} \
	CC="%{__cc}" \
LIBX11="-L%{_prefix}/X11R6/%{_lib} -lXaw -lXmu -lXt -lX11 -lXext -lSM -lICE" \
	%{?with_gtk:LIBGTK="`gtk-config --libs`"} \
	OPT_FLAGS="%{rpmcflags} %{?with_gtk:`gtk-config --cflags`}" \
	<<EOF
2
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_mandir}/man1,%{_bindir},%{_appdefsdir}}

install playmidi xplaymidi $RPM_BUILD_ROOT%{_bindir}
install XPlaymidi.ad $RPM_BUILD_ROOT%{_appdefsdir}/XPlaymidi
install std.o3 drums.o3 std.sb drums.sb $RPM_BUILD_ROOT%{_sysconfdir}
install playmidi.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo '.so playmidi.1' > $RPM_BUILD_ROOT%{_mandir}/man1/xplaymidi.1

%if %{with gtk}
install gtkplaymidi $RPM_BUILD_ROOT%{_bindir}
echo '.so playmidi.1' > $RPM_BUILD_ROOT%{_mandir}/man1/gtkplaymidi.1
%endif

%if %{with svga}
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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/std.o3
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/std.sb
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/drums.o3
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/drums.sb
%{_mandir}/man1/playmidi.1*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xplaymidi
%{_appdefsdir}/XPlaymidi
%{_mandir}/man1/xplaymidi.1*

%if %{with gtk}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtkplaymidi
%{_mandir}/man1/gtkplaymidi.1*
%endif

%if %{with svga}
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/splaymidi
%{_mandir}/man1/splaymidi.1*
%endif
