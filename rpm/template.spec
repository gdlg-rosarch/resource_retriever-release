Name:           ros-lunar-resource-retriever
Version:        1.12.3
Release:        0%{?dist}
Summary:        ROS resource_retriever package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/resource_retriever
Source0:        %{name}-%{version}.tar.gz

Requires:       curl
Requires:       libcurl-devel
Requires:       python-rospkg
Requires:       ros-lunar-rosconsole
Requires:       ros-lunar-roslib
BuildRequires:  curl
BuildRequires:  libcurl-devel
BuildRequires:  ros-lunar-catkin >= 0.5.68
BuildRequires:  ros-lunar-rosconsole
BuildRequires:  ros-lunar-roslib

%description
This package retrieves data from url-format files such as http://, ftp://,
package:// file://, etc., and loads the data into memory. The package:// url for
ros packages is translated into a local file:// url. The resourse retriever was
initially designed to load mesh files into memory, but it can be used for any
type of data. The resource retriever is based on the the libcurl library.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Mon Mar 27 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.3-0
- Autogenerated by Bloom

