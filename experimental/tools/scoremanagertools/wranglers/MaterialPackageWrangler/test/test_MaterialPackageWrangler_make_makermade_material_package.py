import py
from experimental import *


def test_MaterialPackageWrangler_make_makermade_material_package_01():

    wrangler = scoremanagertools.wranglers.MaterialPackageWrangler()
    assert not wrangler.configuration.packagesystem_path_exists('built_in_materials.testsargasso')

    try:
        wrangler.make_makermade_material_package(
            'built_in_materials.testsargasso', 'SargassoMeasureMaterialPackageMaker')
        assert wrangler.configuration.packagesystem_path_exists('built_in_materials.testsargasso')
        mpp = scoremanagertools.materialpackagemakers.SargassoMeasureMaterialPackageMaker('built_in_materials.testsargasso')
        assert mpp.is_makermade
        assert mpp.list_directory() == ['__init__.py', 'tags.py', 'user_input.py']
        assert mpp.has_initializer
        assert not mpp.has_output_material_module
        assert mpp.has_user_input_module
        assert not mpp.initializer_has_output_material_safe_import_statement
        assert not mpp.parent_initializer_has_output_material_safe_import_statement
        assert mpp.output_material is None
    finally:
        mpp.remove()
        assert not wrangler.configuration.packagesystem_path_exists('built_in_materials.testsargasso')


def test_MaterialPackageWrangler_make_makermade_material_package_02():

    wrangler = scoremanagertools.wranglers.MaterialPackageWrangler()
    assert wrangler.configuration.packagesystem_path_exists('built_in_materials.red_numbers')
    assert py.test.raises(Exception,
        "wrangler.make_makermade_material_package('built_in_materials.red_sargasso_measures', "
        "'SargassoMeasureMaterialPackageMaker')")


def test_MaterialPackageWrangler_make_makermade_material_package_03():
    '''Interactively.
    '''

    wrangler = scoremanagertools.wranglers.MaterialPackageWrangler()
    assert not wrangler.configuration.packagesystem_path_exists('built_in_materials.testsargasso')

    try:
        wrangler.make_makermade_material_package_interactively(user_input='sargasso testsargasso q')
        assert wrangler.configuration.packagesystem_path_exists('built_in_materials.testsargasso')
        mpp = scoremanagertools.materialpackagemakers.SargassoMeasureMaterialPackageMaker('built_in_materials.testsargasso')
        assert mpp.is_makermade
        assert mpp.list_directory() == ['__init__.py', 'tags.py', 'user_input.py']
    finally:
        mpp.remove()
        assert not wrangler.configuration.packagesystem_path_exists('built_in_materials.testsargasso')


def test_MaterialPackageWrangler_make_makermade_material_package_04():

    wrangler = scoremanagertools.wranglers.MaterialPackageWrangler()
    assert not wrangler.configuration.packagesystem_path_exists('built_in_materials.testsargasso')

    try:
        tags = {'color': 'red', 'is_colored': True}
        wrangler.make_makermade_material_package(
            'built_in_materials.testsargasso', 'SargassoMeasureMaterialPackageMaker', tags=tags)
        assert wrangler.configuration.packagesystem_path_exists('built_in_materials.testsargasso')
        mpp = scoremanagertools.materialpackagemakers.SargassoMeasureMaterialPackageMaker('built_in_materials.testsargasso')
        assert mpp.is_makermade
        assert mpp.list_directory() == ['__init__.py', 'tags.py', 'user_input.py']
        assert mpp.get_tag('color') == 'red'
        assert mpp.get_tag('is_colored')
    finally:
        mpp.remove()
        assert not wrangler.configuration.packagesystem_path_exists('built_in_materials.testsargasso')
