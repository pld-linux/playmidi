Summary: A MIDI sound file player.
Name: playmidi
Version: 2.4
Release: 7
Source: ftp://ftp.linpeople.org/pub/People/nathan/playmidi-2.4.tar.gz
Source2: awe_voice.h
Copyright: GPL
Group: Applications/Multimedia
Patch0: playmidi-2.3-hertz.patch
Patch1: playmidi-2.3-awe2.patch
Patch2: playmidi-2.4-make.patch
Patch3: playmidi-2.4-midimap.patch
BuildRoot: /var/tmp/playmidi-root

%package X11
Summary: An X Window System based MIDI sound file player.
Requires: playmidi = 2.4
Group: Applications/Multimedia

%description
Playmidi plays MIDI (Musicial Instrument Digital Interface) sound
files through a sound card synthesizer.  This package includes basic
drum samples for use with simple FM synthesizers.

Install playmidi if you want to play MIDI files using your computer's
sound card.

%description X11
Playmidi-X11 provides an X Window System interface for playing MIDI
(Musical Instrument Digital Interface) sound files through a sound
card synthesizer.  This package includes basic drum samples for use
with simple FM synthesizers.

Install playmidi-X11 if you want to use an X interface to play MIDI
sound files using your computer's sound card.

%prep
%setup -q
cp $RPM_SOURCE_DIR/awe_voice.h .
%patch0 -p1 -b .consthertz
%patch1 -p1 -b .awe2
%patch2 -p1 -b .make
%patch3 -p1 -b .midimap

%build
PATH=.:$PATH

%ifarch i386
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
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1,X11R6/bin,X11R6/lib/X11/app-defaults}

install -s -m 755 playmidi $RPM_BUILD_ROOT/usr/bin
install -s -m 755 xplaymidi $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 644 XPlaymidi.ad $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/XPlaymidi

%ifarch i386
install -s -m 755 splaymidi $RPM_BUILD_ROOT/usr/bin
%endif

install -m 644 playmidi.1 $RPM_BUILD_ROOT/usr/man/man1

mkdir -p $RPM_BUILD_ROOT/etc/midi
for n in std.o3 drums.o3 std.sb drums.sb
do
	install -m 644 $n $RPM_BUILD_ROOT/etc/midi/$n
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc QuickStart COPYING BUGS
/usr/bin/playmidi 
%config /etc/midi/std.o3
%config /etc/midi/std.sb
%config /etc/midi/drums.o3
%config /etc/midi/drums.sb
%ifarch i386
/usr/bin/splaymidi
%endif
/usr/man/man1/playmidi.1

%files X11
%defattr(-,root,root)
%config /usr/X11R6/lib/X11/app-defaults/XPlaymidi
/usr/X11R6/bin/xplaymidi
