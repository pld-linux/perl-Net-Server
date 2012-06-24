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
Summary(es):	M�dulo de Perl Net::Server
Summary(fr):	Module Perl Net::Server
Summary(it):	Modulo di Perl Net::Server
Summary(ja):	Net::Server Perl �⥸�塼��
Summary(ko):	Net::Server �� ����
Summary(nb):	Perlmodul Net::Server
Summary(pl):	Modu� Perla Net::Server
Summary(pt_BR):	M�dulo Perl Net::Server
Summary(pt):	M�dulo de Perl Net::Server
Summary(ru):	������ ��� Perl Net::Server
Summary(sv):	Net::Server Perlmodul
Summary(uk):	������ ��� Perl Net::Server
Summary(zh_CN):	Net::Server Perl ģ��
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
Net::Server jest rozszerzalnym, og�lnym silnikiem serwerowym dla
Perla. Net::Server ��czy dobre cechy modu��w Net::Daemon (0.34),
NetServer::Generic (1.03) i Net::FTPServer (1.0), a tak�e r�ne
koncepcje z serwera WWW Apache.

Net::Server pr�buje by� og�lnym serwerem, takim jak Net::Daemon i
NetServer::Generic. Ma mo�liwo�� uruchamiania jako proces inetd
(Net::Server::INET), serwer dla pojedynczego po��czenia (Net::Server
lub Net::Server::Single), serwer forkuj�cy si� (Net::Server::Fork),
serwer preforkuj�cy si� i utrzymuj�cy sta�� liczb� potomk�w
(Net::Server::PreForkSimple) lub jako serwer preforkuj�cy si� i
zarz�dzaj�cy liczb� potomk�w w zale�no�ci od obci��enia serwera
(Net::Server::PreFork). We wszystkich rodzajach opr�cz inetd
serwer ma mo�liwo�� ��czenia na jeden lub wiele port�w.

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
