# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath         grpc.go4.org
%global forgeurl        https://github.com/go4org/grpc
%global commit          11d0a25b491971beb5a4625ea7856a3c4afaafa5

%global common_description %{expand:
Experimental branch of gRPC: a high performance, open source, general RPC 
framework.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        A high performance, open source, general RPC framework
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/golang/glog)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires: golang(golang.org/x/net/http2)
BuildRequires: golang(golang.org/x/net/http2/hpack)
BuildRequires: golang(golang.org/x/net/trace)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/oauth2/jwt)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks -r "clientconn_test\.go"
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md PATENTS CONTRIBUTING.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git11d0a25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1-20180421git11d0a25
- First package for Fedora

