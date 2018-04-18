# Script generated with Bloom
pkgdesc="ROS - This package retrieves data from url-format files such as http://, ftp://, package:// file://, etc., and loads the data into memory. The package:// url for ros packages is translated into a local file:// url. The resourse retriever was initially designed to load mesh files into memory, but it can be used for any type of data. The resource retriever is based on the the libcurl library."
url='http://ros.org/wiki/resource_retriever'

pkgname='ros-melodic-resource-retriever'
pkgver='1.12.4_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'curl'
'ros-melodic-catkin>=0.5.68'
'ros-melodic-rosconsole'
'ros-melodic-roslib'
)

depends=('boost'
'curl'
'python2-rospkg'
'ros-melodic-rosconsole'
'ros-melodic-roslib'
)

conflicts=()
replaces=()

_dir=resource_retriever
source=()
md5sums=()

prepare() {
    cp -R $startdir/resource_retriever $srcdir/resource_retriever
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/melodic/setup.bash ] && source /opt/ros/melodic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/melodic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

