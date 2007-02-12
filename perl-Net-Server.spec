#
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Net-Server
Summary:	Net::Server perl module
Summary(cs.UTF-8):	Modul Net::Server pro Perl
Summary(da.UTF-8):	Perlmodul Net::Server
Summary(de.UTF-8):	Net::Server Perl Modul
Summary(es.UTF-8):	Módulo de Perl Net::Server
Summary(fr.UTF-8):	Module Perl Net::Server
Summary(it.UTF-8):	Modulo di Perl Net::Server
Summary(ja.UTF-8):	Net::Server Perl モジュール
Summary(ko.UTF-8):	Net::Server 펄 모줄
Summary(nb.UTF-8):	Perlmodul Net::Server
Summary(pl.UTF-8):	Moduł Perla Net::Server
Summary(pt.UTF-8):	Módulo de Perl Net::Server
Summary(pt_BR.UTF-8):	Módulo Perl Net::Server
Summary(ru.UTF-8):	Модуль для Perl Net::Server
Summary(sv.UTF-8):	Net::Server Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Net::Server
Summary(zh_CN.UTF-8):	Net::Server Perl 模块
Name:		perl-Net-Server
Version:	0.94
Release:	2
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	2dc5c27056e15b425c9b8421a51fc8dc
URL:		http://search.cpan.org/dist/Net-Server/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Conflicts:	amavisd-new < 1:2.4.1
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

%description -l pl.UTF-8
Net::Server jest rozszerzalnym, ogólnym silnikiem serwerowym dla
Perla. Net::Server łączy dobre cechy modułów Net::Daemon (0.34),
NetServer::Generic (1.03) i Net::FTPServer (1.0), a także różne
koncepcje z serwera WWW Apache.

Net::Server próbuje być ogólnym serwerem, takim jak Net::Daemon i
NetServer::Generic. Ma możliwość uruchamiania jako proces inetd
(Net::Server::INET), serwer dla pojedynczego połączenia (Net::Server
lub Net::Server::Single), serwer forkujący się (Net::Server::Fork),
serwer preforkujący się i utrzymujący stałą liczbę potomków
(Net::Server::PreForkSimple) lub jako serwer preforkujący się i
zarządzający liczbą potomków w zależności od obciążenia serwera
(Net::Server::PreFork). We wszystkich rodzajach oprócz inetd serwer ma
możliwość łączenia na jeden lub wiele portów.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
