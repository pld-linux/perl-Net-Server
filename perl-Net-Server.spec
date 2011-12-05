# TODO
# - Module IO::Multiplex is required for Multiplex. at /usr/share/perl5/vendor_perl/Net/Server/Multiplex.pm line 32.
#   subpkg or add to Requires?
#
# tests hang on udp
%bcond_with	tests	# perform "make test"

%define		pdir	Net
%define		pnam	Net-Server
%include	/usr/lib/rpm/macros.perl
Summary:	Net::Server - extensible, general Perl server engine
Summary(pl.UTF-8):	Net::Server - ogólny, rozszerzalny silnik serwerowy w Perlu
Name:		perl-Net-Server
Version:	0.99
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pnam}-%{version}.tar.gz
# Source0-md5:	1ae03dff8b1009216a2e5d8f4c9a47b1
URL:		http://search.cpan.org/dist/Net-Server/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Suggests:	perl-Net-CIDR
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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Net/Server.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Net/Server/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/Server.pm
%{perl_vendorlib}/Net/Server
%{_mandir}/man3/Net::Server*.3pm*
%{_examplesdir}/%{name}-%{version}
