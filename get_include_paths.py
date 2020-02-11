class get_pybind_include(object):
    """Helper class to determine the pybind11 include path
    The purpose of this class is to postpone importing pybind11
    until it is actually installed, so that the ``get_include()``
    method can be invoked. """

    def __init__(self, user=False):
        self.user = user

    def __str__(self):
        import pybind11
        return pybind11.get_include(self.user)

class get_eigen_include(object):
    """Helper class to determine the pybind11 include path
    The purpose of this class is to postpone importing pybind11
    until it is actually installed, so that the ``get_include()``
    method can be invoked. """
    def __init__(self, user=False):
        self.user = user

    def __str__(self):
        import pybind11
        url = 'https://gitlab.com/libeigen/eigen/-/archive/3.3.7/eigen-3.3.7.tar.gz'
        import wget
        python_path = pybind11.get_include(self.user)
        print(python_path)
        eigen_gz_path = python_path+'/eigen-3.37.tar.gz'

        import os
        if not os.path.exists(eigen_gz_path):
            wget.download(url, eigen_gz_path)

        import tarfile
        if not os.path.exists(python_path + '/eigen-3.3.7'):
            tf = tarfile.open(eigen_gz_path)
            tf.extractall(path=python_path)

        return python_path + '/eigen-3.3.7'

class get_boost_include(object):
    """Helper class to determine the pybind11 include path
    The purpose of this class is to postpone importing pybind11
    until it is actually installed, so that the ``get_include()``
    method can be invoked. """
    def __init__(self, user=False):
        self.user = user

    def __str__(self):
        import pybind11
        url = 'https://dl.bintray.com/boostorg/release/1.72.0/source/boost_1_72_0.tar.gz'
        import wget
        python_path = pybind11.get_include(self.user)
        print(python_path)
        boost_gz_path = python_path+'/boost_1_72_0.tar.gz'

        import os
        if not os.path.exists(boost_gz_path):
            wget.download(url, boost_gz_path)

        import tarfile
        if not os.path.exists(python_path + '/boost_1_72_0'):
            tf = tarfile.open(boost_gz_path)
            tf.extractall(path=python_path)

        return python_path + '/boost_1_72_0'

