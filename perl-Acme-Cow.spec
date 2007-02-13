#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%define		_pacver	0.1
%include	/usr/lib/rpm/macros.perl
%define		pdir	Acme
%define		pnam	Cow
Summary:	Acme::Cow Perl module - talking cow
Summary(pl.UTF-8):	Moduł Perla Acme::Cow - gadająca krowa
Name:		perl-Acme-Cow
Version:	%{_pacver}
Release:	0.9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.nog.net/~tony/warez/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f798f990d5e13c91d5cd85cc4e05d3b7
Source1:	cowsay.sysconfig
Source2:	cowsay.sh
Source3:	cowsay.csh
Patch0:		cowsay-PLD.patch
Patch1:		cowsay-random.patch
URL:		http://www.nog.net/~tony/warez/cowsay.shtml
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Text-Template
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Acme::Cow is the logical evolution of the old cowsay program. Cows are
derived from a base class (Acme::Cow) or from external files.

Cows can be made to say or think many things, optionally filling and
justifying their text out to a given margin.

%description -l pl.UTF-8
Acme::Cow wyewoluował logicznie ze starego programu cowsay. Krowy
pochodzą z klasy bazowej (Acme::Cow) lub z plików zewnętrznych.

Krowy mogą mówić i myśleć o wielu rzeczach, opcjonalnie dopełniając i
wyrównując swój tekst do zadanego marginesu.

%package -n cowsay
Summary:	A Configurable Speaking/Thinking Cow
Summary(pl.UTF-8):	Konfigurowalna mówiąco-myśląca krowa
Version:	4.00
Group:		Applications/Games

%description -n cowsay
cowsay is basically a text filter. Send some text into it, and you get
a cow saying your text. Very easy to use.

%description -n cowsay -l pl.UTF-8
cowsay to prosty filtr tekstowy. Podaje mu się trochę tekstu, a on
wyświetla krowę mówiącą ten tekst. Bardzo proste w użyciu.

%package -n cowsay-on-login
Summary:	Displays cow on login
Summary(pl.UTF-8):	Pokazywanie się krowy przy logowaniu
Version:	4.00
Group:		Applications/Games
Requires:	cowsay
Obsoletes:	cowsay-on-login-static

%description -n cowsay-on-login
If you want a cow to be displayed each time when you log on this
package is what you need.

%description -n cowsay-on-login -l pl.UTF-8
Gdy się chce, żeby krowa pokazywała się przy każdym logowaniu ten
pakiet jest tym, czego potrzeba.

%prep
%setup -q -n %{pdir}-%{pnam}-%{_pacver}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install-cows \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

rm -f $RPM_BUILD_ROOT%{_bindir}/cowthink
ln -s %{_bindir}/cowsay $RPM_BUILD_ROOT%{_bindir}/cowthink

install -d $RPM_BUILD_ROOT%{_sysconfdir}/{profile.d,sysconfig}
install %{SOURCE1}	$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/cowsay
install %{SOURCE2}	$RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install %{SOURCE3}	$RPM_BUILD_ROOT%{_sysconfdir}/profile.d

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
%{_mandir}/man1/cowpm.1p*
%{_datadir}/cows

%files -n cowsay
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cowsay
%attr(755,root,root) %{_bindir}/cowthink
%{_mandir}/man1/cowsay*
%{_mandir}/man1/cowthink*

%files -n cowsay-on-login
%defattr(644,root,root,755)
%attr(755,root,root) /etc/profile.d/cowsay.*sh
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/cowsay
