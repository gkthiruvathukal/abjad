# -*- encoding: utf-8 -*-
import collections
import os
from abjad.tools import iotools
from experimental.tools.scoremanagertools.wranglers.PackageWrangler import \
    PackageWrangler


class SegmentPackageWrangler(PackageWrangler):
    r'''Segment package wrangler.

    ::

        >>> score_manager = scoremanagertools.scoremanager.ScoreManager()
        >>> wrangler = score_manager.segment_package_wrangler
        >>> wrangler
        SegmentPackageWrangler()

    '''

    ### CLASS VARIABLES ###

    asset_storehouse_packagesystem_path_in_built_in_asset_library = None

    score_package_asset_storehouse_path_infix_parts = ('music', 'segments')

    asset_storehouse_packagesystem_path_in_user_asset_library = None

    ### PRIVATE PROPERTIES ###

    @property
    def _breadcrumb(self):
        return 'segments'

    ### PRIVATE METHODS ###

    def _handle_main_menu_result(self, result):
        if result in self.user_input_to_action:
            self.user_input_to_action[result](self)
        else:
            segment_package_proxy = self._initialize_asset_proxy(result)
            segment_package_proxy._run()

    def _make_main_menu(self, head=None):
        main_menu = self.session.io_manager.make_menu(where=self._where)
        asset_section = main_menu.make_asset_section()
        asset_menu_entries = self._make_asset_menu_entries(head=head)
        asset_section.menu_entries = asset_menu_entries
        command_section = main_menu.make_command_section()
        command_section.append(('new segment', 'new'))
        command_section = main_menu.make_command_section()
        command_section.append(('make all pdfs', 'pdfsm'))
        command_section.append(('view all pdfs', 'pdfsv'))
        command_section = main_menu.make_command_section()
        command_section.append(('save all versions', 'versions'))
        return main_menu

    ### PUBLIC PROPERTIES ###

    @property
    def asset_proxy_class(self):
        r'''Asset proxy class of segment package wrangler.

        ::

            >>> wrangler.asset_proxy_class.__name__
            'SegmentPackageProxy'

        Returns class.
        '''
        from experimental.tools import scoremanagertools
        return scoremanagertools.proxies.SegmentPackageProxy

    @property
    def storage_format(self):
        r'''Storage format of segment package wrangler.

        ::

            >>> wrangler.storage_format
            'wranglers.SegmentPackageWrangler()'

        Returns string.
        '''
        return super(SegmentPackageWrangler, self).storage_format

    ### PUBLIC METHODS ###

    def interactively_make_asset_pdfs(
        self,
        pending_user_input=None,
        ):
        self.session.io_manager.assign_user_input(pending_user_input)
        parts = (self.session.current_score_directory_path,)
        parts += self.score_package_asset_storehouse_path_infix_parts
        segments_directory_path = os.path.join(*parts)
        for directory_entry in os.listdir(segments_directory_path):
            if not directory_entry[0].isalpha():
                continue
            segment_package_name = directory_entry
            segment_package_directory_path = os.path.join(
                segments_directory_path,
                segment_package_name,
                )
            segment_package_path = \
                self.configuration.filesystem_path_to_packagesystem_path(
                segment_package_directory_path)
            proxy = self.asset_proxy_class(
                segment_package_path,
                session=self.session,
                )
            proxy.interactively_execute_asset_definition_module(prompt=False)
            output_pdf_file_path = proxy._get_output_pdf_file_path()
            if os.path.isfile(output_pdf_file_path):
                message = 'segment {} PDF created.'
                message = message.format(segment_package_name)
                self.session.io_manager.display(message)
        self.session.io_manager.display('')
        self.interactively_view_asset_pdfs()
        self.session.io_manager.proceed()

    def interactively_view_asset_pdfs(
        self,
        pending_user_input=None,
        ):
        self.session.io_manager.assign_user_input(pending_user_input)
        parts = (self.session.current_score_directory_path,)
        parts += self.score_package_asset_storehouse_path_infix_parts
        segments_directory_path = os.path.join(*parts)
        output_pdf_file_paths = []
        for directory_entry in os.listdir(segments_directory_path):
            if not directory_entry[0].isalpha():
                continue
            segment_package_name = directory_entry
            output_pdf_file_path = os.path.join(
                segments_directory_path,
                segment_package_name,
                'output.pdf',
                )
            if os.path.isfile(output_pdf_file_path):
                output_pdf_file_paths.append(output_pdf_file_path)
        command = ' '.join(output_pdf_file_paths)
        command = 'open ' + command
        iotools.spawn_subprocess(command)

    def interactively_version_all_assets(
        self,
        pending_user_input=None,
        ):
        self.session.io_manager.assign_user_input(pending_user_input)
        parts = (self.session.current_score_directory_path,)
        parts += self.score_package_asset_storehouse_path_infix_parts
        segments_directory_path = os.path.join(*parts)
        for directory_entry in os.listdir(segments_directory_path):
            if not directory_entry[0].isalpha():
                continue
            segment_package_name = directory_entry
            segment_package_directory_path = os.path.join(
                segments_directory_path,
                segment_package_name,
                )
            segment_package_path = \
                self.configuration.filesystem_path_to_packagesystem_path(
                segment_package_directory_path)
            proxy = self.asset_proxy_class(
                segment_package_path,
                session=self.session,
                )
            version_number = proxy.interactively_save_to_versions_directory(
                is_interactive=False,
                )
            if version_number is not None:
                message = 'segment {} version {} written to disk.'
                message = message.format(segment_package_name, version_number)
                self.session.io_manager.display(message)
        self.session.io_manager.display('')
        self.session.io_manager.proceed()

    def list_asset_filesystem_paths(
        self,
        in_built_in_asset_library=True, 
        in_user_asset_library=True,
        in_built_in_score_packages=True, 
        in_user_score_packages=True, 
        head=None,
        ):
        r'''Lists asset filesystem paths.

        Example. List built-in segment package filesystem paths:

        ::

            >>> for x in wrangler.list_asset_filesystem_paths(
            ...     in_user_asset_library=False, 
            ...     in_user_score_packages=False,
            ...     ):
            ...     x
            '.../blue_example_score/music/segments/segment_01'
            '.../blue_example_score/music/segments/segment_02'
            '.../red_example_score/music/segments/segment_01'
            '.../red_example_score/music/segments/segment_02'
            '.../red_example_score/music/segments/segment_03'

        Returns list.
        '''
        superclass = super(SegmentPackageWrangler, self)
        return superclass.list_asset_filesystem_paths(
            in_built_in_asset_library=in_built_in_asset_library,
            in_user_asset_library=in_user_asset_library,
            in_built_in_score_packages=in_built_in_score_packages,
            in_user_score_packages=in_user_score_packages,
            head=head,
            )

    def list_asset_names(
        self,
        in_built_in_asset_library=True, 
        in_user_asset_library=True,
        in_built_in_score_packages=True, 
        in_user_score_packages=True, 
        head=None,
        ):
        r'''Lists asset names.

        Example 1. List built-in segment package names:

        ::

            >>> for x in wrangler.list_asset_names(
            ...     in_user_asset_library=False, 
            ...     in_user_score_packages=False,
            ...     ):
            ...     x
            'segment 01'
            'segment 02'
            'segment 01'
            'segment 02'
            'segment 03'

        Example 2. List red example score segment package names:

            >>> head = 'experimental.tools.scoremanagertools.scorepackages.red_example_score'
            >>> for x in wrangler.list_asset_names(head=head):
            ...     x
            'segment 01'
            'segment 02'
            'segment 03'

        Returns list.
        '''
        superclass = super(SegmentPackageWrangler, self)
        return superclass.list_asset_names(
            in_built_in_asset_library=in_built_in_asset_library,
            in_user_asset_library=in_user_asset_library,
            in_built_in_score_packages=in_built_in_score_packages,
            in_user_score_packages=in_user_score_packages,
            head=head,
            )

    def list_asset_packagesystem_paths(
        self,
        in_built_in_asset_library=True, 
        in_user_asset_library=True,
        in_built_in_score_packages=True, 
        in_user_score_packages=True, 
        head=None,
        ):
        r'''Lists asset packagesystem paths.

        Example. List built-in segment package paths:

        ::

            >>> for x in wrangler.list_asset_packagesystem_paths(
            ...     in_user_asset_library=False, 
            ...     in_user_score_packages=False):
            ...     x
            '....blue_example_score.music.segments.segment_01'
            '....blue_example_score.music.segments.segment_02'
            '....red_example_score.music.segments.segment_01'
            '....red_example_score.music.segments.segment_02'
            '....red_example_score.music.segments.segment_03'

        Returns list.
        '''
        superclass = super(SegmentPackageWrangler, self)
        return superclass.list_asset_packagesystem_paths(
            in_built_in_asset_library=in_built_in_asset_library,
            in_user_asset_library=in_user_asset_library,
            in_built_in_score_packages=in_built_in_score_packages,
            in_user_score_packages=in_user_score_packages,
            head=head,
            )

    def list_asset_proxies(
        self,
        in_built_in_asset_library=True, 
        in_user_asset_library=True,
        in_built_in_score_packages=True, 
        in_user_score_packages=True, 
        head=None,
        ):
        r'''Lists asset proxies.

        Example 1. List built-in segment package proxies:

        ::

            >>> for x in wrangler.list_asset_proxies(
            ...     in_user_asset_library=False, 
            ...     in_user_score_packages=False):
            ...     x
            SegmentPackageProxy('.../blue_example_score/music/segments/segment_01')
            SegmentPackageProxy('.../blue_example_score/music/segments/segment_02')
            SegmentPackageProxy('.../red_example_score/music/segments/segment_01')
            SegmentPackageProxy('.../red_example_score/music/segments/segment_02')
            SegmentPackageProxy('.../red_example_score/music/segments/segment_03')

        Example 2. List red example score segment package proxies:

        ::

            >>> head = 'experimental.tools.scoremanagertools.scorepackages.red_example_score'
            >>> for x in wrangler.list_asset_proxies(head=head):
            ...     x
            SegmentPackageProxy('.../red_example_score/music/segments/segment_01')
            SegmentPackageProxy('.../red_example_score/music/segments/segment_02')
            SegmentPackageProxy('.../red_example_score/music/segments/segment_03')

        Returns list.
        '''
        superclass = super(SegmentPackageWrangler, self)
        return superclass.list_asset_proxies(
            in_built_in_asset_library=in_built_in_asset_library,
            in_user_asset_library=in_user_asset_library,
            in_built_in_score_packages=in_built_in_score_packages,
            in_user_score_packages=in_user_score_packages,
            head=head,
            )

    def list_asset_storehouse_filesystem_paths(
        self,
        in_built_in_asset_library=True, 
        in_user_asset_library=True,
        in_built_in_score_packages=True, 
        in_user_score_packages=True,
        ):
        r'''Lists asset storehouse filesystem paths.

        Example. List built-in segment package storehouse filesystem paths:

        ::

            >>> for x in wrangler.list_asset_storehouse_filesystem_paths(
            ...     in_user_asset_library=False, 
            ...     in_user_score_packages=False,
            ...     ):
            ...     x
            '.../blue_example_score/music/segments'
            '.../green_example_score/music/segments'
            '.../red_example_score/music/segments'

        Returns list.
        '''
        superclass = super(SegmentPackageWrangler, self)
        return superclass.list_asset_storehouse_filesystem_paths(
            in_built_in_asset_library=in_built_in_asset_library,
            in_user_asset_library=in_user_asset_library,
            in_built_in_score_packages=in_built_in_score_packages,
            in_user_score_packages=in_user_score_packages,
            )

    def make_asset(
        self, 
        package_path, 
        is_interactive=False, 
        tags=None,
        ):
        r'''Makes package.

        Returns none.
        '''
        tags = collections.OrderedDict(tags or {})
        directory_path = \
            self.configuration.packagesystem_path_to_filesystem_path(
            package_path)
        assert not os.path.exists(directory_path)
        os.mkdir(directory_path)
        proxy = self.asset_proxy_class(
            packagesystem_path=package_path,
            session=self.session,
            )
        proxy.write_initializer_to_disk()
        proxy.write_segment_definition_module_to_disk()
        proxy.make_versions_directory()
        line = 'package {!r} created.'.format(package_path)
        self.session.io_manager.proceed(line, is_interactive=is_interactive)

    ### UI MANIFEST ###

    user_input_to_action = PackageWrangler.user_input_to_action.copy()
    user_input_to_action.update({
        'pdfsm': interactively_make_asset_pdfs,
        'pdfsv': interactively_view_asset_pdfs,
        'versions': interactively_version_all_assets,
        })
