Summary: A MIDI sound file player.
Summary(pl): Odtwarzacz plików MIDI.
Name: playmidi
Version: 2.4
Release: 8
Source: ftp://ftp.linpeople.org/pub/People/nathan/playmidi-2.4.tar.gz
Copyright: GPL
Group: Applications/Sound
Group(pl): Aplikacje/D¼wiêk
Patch0: playmidi-2.3-hertz.patch
Patch1: playmidi-2.4-make.patch
Patch2: playmidi-2.4-midimap.patch
Patch3: playmidi-2.4-glibconfig.patch
BuildRoot: /var/tmp/playmidi-root

%package X11
Summary: An X Window System based MIDI sound file player.
Summary(pl): Odtwarzacz plików MIDI dla systemu X Window
Requires: playmidi = 2.4
Group: Applications/Multimedia
Group(pl): Aplikacje/D¼wiêk

%package svga
Summary: An SVGAlib based MIDI sound file player.
Summary(pl): Odtwarzacz plików MIDI wykorzystuj±cy SVGAlib.
Requires: playmidi = 2.4
Group: Applications/Multimedia
Group(pl): Aplikacje/D¼wiêk
ExclusiveArch: %ix86

%description
Playmidi plays MIDI (Musicial Instrument Digital Interface) sound
files through a sound card synthesizer.  This package includes basic
drum samples for use with simple FM synthesizers.

Install playmidi if you want to play MIDI files using your computer's
sound card.

%description -l pl
Playmidi odtwarza pliki MIDI poprzez syntetyzer karty d¼wiêkowej.
Pakiet zawiera podstawowe instrumenty perkusyjne do wykorzystania z
prostymi syntetyzerami FM.

%description X11
Playmidi-X11 provides an X Window System interface for playing MIDI
(Musical Instrument Digital Interface) sound files through a sound
card synthesizer.

Install playmidi-X11 if you want to use an X interface to play MIDI
sound files using your computer's sound card.

%description X11 -l pl
Playmidi-X11 dostarcza interfejs opary o system X Window umo¿liwiaj±cy
odtwarzanie plików MIDI poprzez kartê d¼wiêkow±.

%description svga
Playmidi-svga provides an SVGAlib interface for playing MIDI (Musical
Instrument Digital Interface) sound files through a sound card
synthesizer.

Install playmidi-svga if you want to use an SVGAlib interface to play
MIDI sound files using your computer's sound card.

%description svga -l pl
Playmidi-svga dostarcza interfejs oparty o SVGAlib umo¿liwiaj±cy
odtwarzanie plików MIDI poprzez kartê d¼wiêkow±.

%prep
%setup -q
# awe_voice.h is now part of the kernel source.
rm awe_voice.h
%patch0 -p1 -b .consthertz
%patch1 -p1 -b .make
%patch2 -p1 -b .midimap
%patch3 -p1 -b .glibconfig
%build
PATH=.:$PATH

%ifarch %ix86
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" playmidi splaymidi xplaymidi <<EOF
2
EOF
%else
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" playmidi xplaymidi <<EOF
2
EOF
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/{midi}
mkdir -p $RPM_BUILD_ROOT/usr/{bin,X11R6/bin,X11R6/lib/X11/app-defaults}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -s -m 755 playmidi $RPM_BUILD_ROOT/usr/bin
install -s -m 755 xplaymidi $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 644 XPlaymidi.ad $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/XPlaymidi

%ifarch %ix86
install -s -m 755 splaymidi $RPM_BUILD_ROOT/usr/bin
%endif

install -m 644 playmidi.1 $RPM_BUILD_ROOT%{_mandir}/man1
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/*\
	BUGS COPYING QuickStart

mkdir -p $RPM_BUILD_ROOT/etc/midi
for n in std.o3 drums.o3 std.sb drums.sb
do
	install -m 644 $n $RPM_BUILD_ROOT/etc/midi/$n
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {QuickStart,COPYING,BUGS}.gz
/usr/bin/playmidi 
%config /etc/midi/std.o3
%config /etc/midi/std.sb
%config /etc/midi/drums.o3
%config /etc/midi/drums.sb
%{_mandir}/man1/playmidi.1.gz

%files X11
%defattr(644,root,root,755)
%config /usr/X11R6/lib/X11/app-defaults/XPlaymidi
/usr/X11R6/bin/xplaymidi

%files svga
%defattr(644,root,root,755)
%attr(4644,root,root)/usr/bin/splaymidi
