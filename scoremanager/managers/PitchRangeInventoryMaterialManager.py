# -*- encoding: utf-8 -*-
from abjad import *
from scoremanager.managers.MaterialManager import MaterialManager
from scoremanager.editors.PitchRangeInventoryEditor \
    import PitchRangeInventoryEditor


class PitchRangeInventoryMaterialManager(MaterialManager):

    ### CLASS VARIABLES ###

    generic_output_name = 'pitch range inventory'

    _output_material_checker = staticmethod(
        lambda x: isinstance(x, pitchtools.PitchRangeInventory))

    _output_material_editor = PitchRangeInventoryEditor

    _output_material_maker = pitchtools.PitchRangeInventory

    _output_material_module_import_statements = [
        'from abjad import *',
        ]

    ### PUBLIC METHODS ###

    @staticmethod
    def __illustrate__(pitch_range_inventory, **kwargs):
        chords = []
        for pitch_range in pitch_range_inventory:
            chord = Chord(
                (pitch_range.start_pitch, pitch_range.stop_pitch), 
                Duration(1))
            chords.append(chord)
        score, treble_staff, bass_staff = \
            scoretools.make_piano_score_from_leaves(chords)
        illustration = lilypondfiletools.make_basic_lilypond_file(score)
        rests = iterate(score).by_class(Rest)
        scoretools.replace_leaves_in_expr_with_skips(list(rests))
        override(score).time_signature.stencil = False
        override(score).bar_line.transparent = True
        override(score).span_bar.transparent = True
        set_(score).proportional_notation_duration = \
            schemetools.SchemeMoment(1, 4)
        return illustration
