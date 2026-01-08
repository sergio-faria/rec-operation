from setuptools import find_packages, setup

setup(
	name='rec_op_lem_prices',
	packages=find_packages(include=['rec_op_lem_prices', 'rec_op_lem_prices.*']),
	version='0.2.7',
	description='REC Management Tool for optimal operation of REC and LEM price definition.',
	author='ricardo.emanuel@inesctec.pt',
	install_requires=[
    'joblib~=1.3.2',
    'loguru~=0.7.2',
    'matplotlib~=3.7.0',          # Já estava correto
    'numpy~=1.24.0',              # CORRIGIDO (de 1.26.1)
    'pandas~=1.5.0',              # CORRIGIDO (de 2.1.2)
    'pulp~=2.7.0',
    'scikit-learn~=1.3.0',        # CORRIGIDO (de 1.4.1.post1)
    'setuptools~=80.9.0',           # CORRIGIDO (de 70.0.0)
    'typing-extensions~=4.10.0'
],
	setup_requires=['pytest_runner==6.0.0'],
	tests_require=['pytest==7.4.2'],
	test_suite='tests'
)
