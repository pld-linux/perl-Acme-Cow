#
# Conditional build:
# _without_tests - do not perform "make test"
#
%define		_pacver	0.1
%include	/usr/lib/rpm/macros.perl
%define	pdir	Acme
%define	pnam	Cow
Summary:	Acme::Cow perl module - talking cow
Summary(pl):	Modu³ perla Acme::Cow - gadaj±ca krowa
Name:		perl-Acme-Cow
Version:	%{_pacver}
Release:	0.9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.nog.net/~tony/warez/%{pdir}-%{pnam}-%{version}.tar.gz
Source1:        cowsay.sysconfig
Source2:        cowsay.sh
Source3:        cowsay.csh
Patch0:         cowsay-PLD.patch
Patch1:         cowsay-random.patch
URL:		http://www.nog.net/~tony/warez/cowsay.shtml
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Text-Template
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Acme::Cow - Perl interface to talking cow.

%description -l pl
Acme::Cow - interfejs perla dla gadaj±cej krowy.

%package -n cowsay
Summary:        A Configurable Speaking/Thinking Cow
Summary(pl):    Konfigurowalna mówi±co-my¶l±ca krowa
Version:        4.00
Group:          Applications/Games

%description -n cowsay
cowsay is basically a text filter. Send some text into it, and you get
a cow saying your text. Very easy to use.
                                                                                
%description -n cowsay -l pl
cowsay to prosty filtr tekstowy. Podaje mu siê trochê tekstu, a on
wy¶wietla krowê mówi±c± ten tekst. Bardzo proste w u¿yciu.

%package -n cowsay-on-login
Summary:        Displays cow on login
Summary(pl):    Wy¶wietlanie krowy przy logowaniu
Version:	4.00
Group:          Applications/Games
Requires:       cowsay
Obsoletes:	cowsay-on-login-static

%description -n cowsay-on-login
If you want a cow to be displayed each time when you log on this
package is what you need.
                                                                                
%description -n cowsay-on-login -l pl
Je¶li chcesz, ¿eby krowa by³a wy¶wietlana przy ka¿dym logowaniu ten
pakiet jest tym, czego potrzebujesz.

%prep
%setup -q -n %{pdir}-%{pnam}-%{_pacver}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install-cows \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

rm -f $RPM_BUILD_ROOT/%{_bindir}/cowthink
ln -s %{_bindir}/cowsay $RPM_BUILD_ROOT/%{_bindir}/cowthink

install -d $RPM_BUILD_ROOT/%{_sysconfdir}/{profile.d,sysconfig}
install %{SOURCE1}	$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/cowsay
install %{SOURCE2}	$RPM_BUILD_ROOT%{_sysconfdir}/profile.d/
install %{SOURCE3}	$RPM_BUILD_ROOT%{_sysconfdir}/profile.d/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
# use macros:
#%{perl_vendorlib}/Acme/Cow.pm
%{perl_vendorlib}/Acme
#%%{perl_vendorarch}/...
%attr(755,root,root) %{_bindir}/cowpm
%{_mandir}/man3/*
%{_mandir}/man1/cowpm.1p.gz
%{_datadir}/cows

%files -n cowsay
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cowsay
%attr(755,root,root) %{_bindir}/cowthink
%{_mandir}/man1/cowsay*
%{_mandir}/man1/cowthink*

%files -n cowsay-on-login
%defattr(644,root,root,755)
%attr(755,root,root) /%{_sysconfdir}/profile.d/cowsay.*sh
%config(noreplace) %verify(not size mtime md5) /%{_sysconfdir}/sysconfig/cowsay
