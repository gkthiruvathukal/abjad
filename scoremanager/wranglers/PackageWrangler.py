# -*- encoding: utf-8 -*-
import os
from abjad.tools import sequencetools
from abjad.tools import stringtools
from scoremanager.wranglers.Wrangler import Wrangler


class PackageWrangler(Wrangler):
    r'''Package wrangler.
    '''

    ### INITIALIZER ###

    def __init__(self, session=None):
        from scoremanager import managers
        Wrangler.__init__(self, session=session)
        self._asset_manager_class = managers.PackageManager

    ### PRIVATE PROPERTIES ###

    @property
    def _current_storehouse_package_path(self):
        path = self._current_storehouse_directory_path
        package = self._configuration.path_to_package(path)
        return package

    @property
    def _temporary_asset_manager(self):
        return self._initialize_asset_manager(
            self._temporary_asset_package_path)

    @property
    def _temporary_asset_name(self):
        return '__temporary_package'

    @property
    def _temporary_asset_package_path(self):
        path = self._temporary_asset_filesystem_path
        package = self._configuration.path_to_package(path)
        return package

    @property
    def _user_input_to_action(self):
        superclass = super(PackageWrangler, self)
        _user_input_to_action = superclass._user_input_to_action
        _user_input_to_action = _user_input_to_action.copy()
        _user_input_to_action.update({
            'new': self.make_asset,
            'ren': self.rename,
            })
        return _user_input_to_action

    ### PRIVATE METHODS ###

    def _handle_main_menu_result(self, result):
        self._io_manager.print_not_yet_implemented()

    def _initialize_asset_manager(self, filesystem_path):
        if os.path.sep not in filesystem_path:
            filesystem_path = self._configuration.package_to_path(
                filesystem_path)
        manager = self._asset_manager_class(
            filesystem_path=filesystem_path, 
            session=self._session,
            )
        return manager

    def _is_valid_directory_entry(self, expr):
        superclass = super(PackageWrangler, self)
        if superclass._is_valid_directory_entry(expr):
            if '.' not in expr:
                return True
        return False

    def _list_asset_managers(
        self,
        abjad_library=True,
        user_library=True,
        abjad_score_packages=True,
        user_score_packages=True,
        head=None,
        ):
        r'''Lists asset managers.

        Returns list.
        '''
        result = []
        for package_path in self._list_asset_package_paths(
            abjad_library=abjad_library,
            user_library=user_library,
            abjad_score_packages=abjad_score_packages,
            user_score_packages=user_score_packages,
            head=head,
            ):
            asset_manager = self._initialize_asset_manager(package_path)
            result.append(asset_manager)
        return result

    def _list_asset_package_paths(
        self,
        abjad_library=True,
        user_library=True,
        abjad_score_packages=True,
        user_score_packages=True,
        head=None,
        ):
        r'''Lists asset packagesystem paths.

        Returns list.
        '''
        result = []
        for filesystem_path in self._list_asset_filesystem_paths(
            abjad_library=abjad_library,
            user_library=user_library,
            abjad_score_packages=abjad_score_packages,
            user_score_packages=user_score_packages,
            head=head):
            package_path = \
                self._configuration.path_to_package(
                    filesystem_path)
            result.append(package_path)
        return result

    def _list_storehouse_package_paths(
        self,
        abjad_library=True,
        user_library=True,
        abjad_score_packages=True,
        user_score_packages=True,
        ):
        r'''Lists asset storehouse packagesystem paths.

        Returns list.
        '''
        result = []
        superclass = super(PackageWrangler, self)
        for filesystem_path in \
            superclass._list_storehouse_directory_paths(
            abjad_library=True,
            user_library=True,
            abjad_score_packages=True,
            user_score_packages=True,
            ):
            package_path = \
                self._configuration.path_to_package(
                filesystem_path)
            result.append(package_path)
        return result

    def _list_visible_asset_package_paths(self, head=None):
        r'''Lists visible asset packagesystem paths.

        Returns list.
        '''
        result = []
        if hasattr(self, '_list_visible_asset_managers'):
            for asset_manager in self._list_visible_asset_managers(head=head):
                result.append(asset_manager._package_path)
        else:
            for asset_manager in self._list_asset_managers(
                abjad_library=True,
                user_library=True,
                abjad_score_packages=True,
                user_score_packages=True,
                head=head,
                ):
                result.append(asset_manager._package_path)
        return result

    def _make_asset(self, asset_name):
        assert stringtools.is_snake_case_package_name(asset_name)
        asset_filesystem_path = os.path.join(
            self._current_storehouse_directory_path, asset_name)
        os.mkdir(asset_filesystem_path)
        package_manager = self._initialize_asset_manager(asset_name)
        package_manager.fix(prompt=False)

    # TODO: reduce indentation with early return statements
    def _make_asset_menu_entries(self, head=None):
        names = self._list_asset_names(head=head)
        keys = len(names) * [None]
        prepopulated_return_values = len(names) * [None]
        paths = self._list_visible_asset_package_paths(head=head)
        assert len(names) == len(keys) == len(paths)
        if names:
            sequences = (names, [None], [None], paths)
            entries = sequencetools.zip_sequences(sequences, cyclic=True)
            package_manager = self._current_package_manager
            if package_manager:
                view_name = package_manager._get_metadatum('view_name')
                if view_name:
                    view_inventory = self._read_view_inventory_from_disk()
                    if view_inventory:
                        correct_view = view_inventory.get(view_name)
                        if correct_view:
                            entries = \
                                self._sort_asset_menu_entries_by_view(
                                entries,
                                correct_view,
                                )
            return entries

    def _make_main_menu(self, head=None):
        self._io_manager.print_not_yet_implemented()

    @staticmethod
    def _sort_asset_menu_entries_by_view(entries, view):
        entries_found_in_view = len(entries) * [None]
        entries_not_found_in_view = []
        for entry in entries:
            name = entry[0]
            if name in view:
                index = view.index(name)
                entries_found_in_view[index] = entry
            else:
                entries_not_found_in_view.append(entry)
        entries_found_in_view = [
            x for x in entries_found_in_view 
            if not x is None
            ]
        sorted_entries = entries_found_in_view + entries_not_found_in_view
        assert len(sorted_entries) == len(entries)
        return sorted_entries

    ### PUBLIC METHODS ###

    def get_available_package_path(
        self, 
        pending_user_input=None,
        ):
        r'''Gets available packagesystem path.

        Returns string.
        '''
        self._io_manager._assign_user_input(pending_user_input)
        while True:
            getter = self._io_manager.make_getter(where=self._where)
            getter.append_space_delimited_lowercase_string('name')
            with self._backtracking:
                package = getter._run()
            if self._session._backtrack():
                return
            package = stringtools.string_to_accent_free_snake_case(package)
            path = os.path.join(
                self._current_storehouse_directory_path, 
                package,
                )
            package = self._configuration.path_to_package(path)
            if self._configuration.package_exists(package):
                line = 'package already exists: {!r}.'
                line = line.format(path)
                self._io_manager.display([line, ''])
            else:
                return package

    def make_asset(
        self,
        pending_user_input=None,
        ):
        r'''Makes asset.

        Returns none.
        '''
        self._io_manager._assign_user_input(pending_user_input)
        with self._backtracking:
            package_path = \
                self.get_available_package_path()
        if self._session._backtrack():
            return
        self._make_asset(package_path)

    def make_empty_package(self, package_path):
        r'''Makes empty package.

        Returns none.
        '''
        if package_path is None:
            return
        directory_path = \
            self._configuration.package_to_path(
            package_path)
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)
            initializer_file_path = os.path.join(
                directory_path, '__init__.py')
            file_reference = file(initializer_file_path, 'w')
            file_reference.write('')
            file_reference.close()

    def rename(self, head=None, pending_user_input=None):
        r'''Renames asset.

        Returns none.
        '''
        self._io_manager._assign_user_input(pending_user_input)
        with self._backtracking:
            asset_package_path = self.select_asset_package_path(
                head=head, 
                infinitival_phrase='to rename',
                )
        if self._session._backtrack():
            return
        asset_manager = self._initialize_asset_manager(asset_package_path)
        asset_manager.rename()

    def select_asset_package_path(
        self,
        clear=True,
        cache=False,
        head=None,
        infinitival_phrase=None,
        pending_user_input=None,
        ):
        '''Selects asset packagesystem path.

        Returns string.
        '''
        self._io_manager._assign_user_input(pending_user_input)
        self._session._cache_breadcrumbs(cache=cache)
        while True:
            name = '_human_readable_target_name'
            human_readable_target_name = getattr(self, name, None)
            breadcrumb = self._make_asset_selection_breadcrumb(
                human_readable_target_name=human_readable_target_name,
                infinitival_phrase=infinitival_phrase,
                )
            self._session._push_breadcrumb(breadcrumb)
            menu = self._make_asset_selection_menu(head=head)
            result = menu._run(clear=clear)
            if self._session._backtrack():
                break
            elif not result:
                self._session._pop_breadcrumb()
                continue
            else:
                break
        self._session._pop_breadcrumb()
        self._session._restore_breadcrumbs(cache=cache)
        return result
