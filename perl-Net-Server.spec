#
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Net-Server
Summary:	Net::Server perl module
Summary(cs):	Modul Net::Server pro Perl
Summary(da):	Perlmodul Net::Server
Summary(de):	Net::Server Perl Modul
Summary(es):	Módulo de Perl Net::Server
Summary(fr):	Module Perl Net::Server
Summary(it):	Modulo di Perl Net::Server
Summary(ja):	Net::Server Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Net::Server ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Net::Server
Summary(pl):	Modu³ Perla Net::Server
Summary(pt_BR):	Módulo Perl Net::Server
Summary(pt):	Módulo de Perl Net::Server
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Net::Server
Summary(sv):	Net::Server Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Net::Server
Summary(zh_CN):	Net::Server Perl Ä£¿é
Name:		perl-Net-Server
Version:	0.90
Release:	0.1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	6874fc7b37ee2969aba03f1ccebbe6a3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Net::Server" is an extensible, generic Perl server engine.
"Net::Server" combines the good properties from "Net::Daemon" (0.34),
"NetServer::Generic" (1.03), and "Net::FTPServer" (1.0), and also from
various concepts in the Apache Webserver.

"Net::Server" attempts to be a generic server as in "Net::Daemon" and
"NetServer::Generic". It includes with it the ability to run as an
inetd process ("Net::Server::INET"), a single connection server
("Net::Server" or "Net::Server::Single"), a forking server
("Net::Server::Fork"), a preforking server which maintains a constant
number of preforked children ("Net::Server::PreForkSimple"), or as a
managed preforking server which maintains the number of children based
on server load ("Net::Server::PreFork"). In all but the inetd type,
the server provides the ability to connect to one or to multiple
server ports.

%description -l pl
Net::Server jest rozszerzalnym, ogólnym silnikiem serwerowym dla
Perla. Net::Server ³±czy dobre cechy modu³ów Net::Daemon (0.34),
NetServer::Generic (1.03) i Net::FTPServer (1.0), a tak¿e ró¿ne
koncepcje z serwera WWW Apache.

Net::Server próbuje byæ ogólnym serwerem, takim jak Net::Daemon i
NetServer::Generic. Ma mo¿liwo¶æ uruchamiania jako proces inetd
(Net::Server::INET), serwer dla pojedynczego po³±czenia (Net::Server
lub Net::Server::Single), serwer forkuj±cy siê (Net::Server::Fork),
serwer preforkuj±cy siê i utrzymuj±cy sta³± liczbê potomków
(Net::Server::PreForkSimple) lub jako serwer preforkuj±cy siê i
zarz±dzaj±cy liczb± potomków w zale¿no¶ci od obci±¿enia serwera
(Net::Server::PreFork). We wszystkich rodzajach oprócz inetd
serwer ma mo¿liwo¶æ ³±czenia na jeden lub wiele portów.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README examples
%{perl_vendorlib}/Net/Server*
%{_mandir}/man3/*
