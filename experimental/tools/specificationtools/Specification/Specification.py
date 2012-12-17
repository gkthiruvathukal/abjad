import abc
import numbers
from abjad.tools import *
from experimental.tools import helpertools
from experimental.tools import requesttools
from experimental.tools import settingtools
from experimental.tools import symbolictimetools
from experimental.tools.symbolictimetools.SymbolicTimespan import SymbolicTimespan


class Specification(SymbolicTimespan):
    r'''.. versionadded:: 1.0

    ::

        >>> from experimental.tools import *

    Abstract base class from which concrete specification classes inherit.

    Score and segment specifications constitute the primary vehicle of composition.

    Composers make settings against score and segment specifications.

    Interpreter code interprets score and segment specifications.

    Abjad score object results from interpretation.

    The examples below reference the following segment specification::

        >>> score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=4)
        >>> score_specification = specificationtools.ScoreSpecification(score_template=score_template)
        
    ::
    
        >>> red_segment = score_specification.append_segment(name='red')

    ::
            
        >>> red_segment
        SegmentSpecification('red')

    Return specification instance.
    '''

    ### CLASS ATTRIBUTES ###

    __metaclass__ = abc.ABCMeta

    attributes = helpertools.AttributeNameEnumeration()

    ### INITIALIZER ###

    @abc.abstractmethod
    def __init__(self, score_specification, score_template):
        from experimental.tools import specificationtools
        SymbolicTimespan.__init__(self)
        self._score_specification = score_specification
        self._score_template = score_template
        self._score_model = score_template()
        self._abbreviated_context_names = []
        self._context_names = []
        self._multiple_context_settings = settingtools.MultipleContextSettingInventory()
        self._single_context_settings_by_context = specificationtools.ContextProxyDictionary(score_template())
        self._initialize_context_name_abbreviations()
        self._contexts = specificationtools.ContextProxyDictionary(score_template())
        self._single_context_settings = settingtools.SingleContextSettingInventory()

    ### READ-ONLY PRIVATE PROPERTIES ###

    @property
    def _timespan_abbreviation(self):
        '''Form of symbolic timespan suitable for writing to disk.
        
        Specifications alias this property to specification name.
        '''
        return self.specification_name

    ### PRIVATE METHODS ###

    def _clone(self):
        return self.select()

    def _context_token_to_context_names(self, context_token):
        if context_token is None:
            context_names = [self.score_name] 
        elif context_token == [self.score_name]:
            context_names = context_token
        elif isinstance(context_token, type(self)):
            context_names = [context_token.score_name]
        elif context_token in self.abbreviated_context_names:
            context_names = [context_token]
        elif isinstance(context_token, (tuple, list)) and all([
            x in self.abbreviated_context_names for x in context_token]):
            context_names = context_token
        elif isinstance(context_token, contexttools.Context):
            context_names = [context_token.name]
        elif contexttools.all_are_contexts(context_token):
            context_names = [context.name for context in context_token]
        else:
            raise ValueError('invalid context token: {!r}'.format(context_token))
        return context_names

    def _initialize_context_name_abbreviations(self):
        self.context_name_abbreviations = getattr(self.score_template, 'context_name_abbreviations', {})
        for context_name_abbreviation, context_name in self.context_name_abbreviations.iteritems():
            setattr(self, context_name_abbreviation, context_name)
            self._abbreviated_context_names.append(context_name)
        score = self.score_template()
        self._score_name = score.name
        for context in iterationtools.iterate_contexts_in_expr(score):
            if hasattr(context, 'name'):
                self._context_names.append(context.name)

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def abbreviated_context_names(self):
        return self._abbreviated_context_names

    @property
    def context_names(self):
        return self._context_names

    @property
    def contexts(self):
        return self._contexts

    @property
    def multiple_context_settings(self):
        '''Secification multiple-context settings.

        Return multiple-context setting inventory.
        '''
        return self._multiple_context_settings

    @property
    def score_model(self):
        '''Secification score model.

        Return Abjad score object.
        '''
        return self._score_model

    @property
    def score_name(self):
        return self._score_name

    @abc.abstractproperty
    def score_specification(self):
        pass

    @property
    def score_template(self):
        return self._score_template

    @property
    def single_context_settings(self):
        return self._single_context_settings

    @property
    def single_context_settings_by_context(self):
        return self._single_context_settings_by_context

    ### PUBLIC METHODS ###

    # TODO: replace 'timespan', 'edge', 'multiplier' keywords and with (symbolic) 'offset' keyword.
    def request_division_command(self, voice, 
        timespan=None, edge=None, multiplier=None, addendum=None, reverse=None):
        r'''Request segment division command active at offset
        in `voice`.

        Example 1. Request division command active at start of segment::

            >>> request = red_segment.request_division_command('Voice 1')

        ::

            >>> z(request)
            requesttools.CommandRequest(
                'divisions',
                'Voice 1',
                symbolictimetools.SymbolicOffset(
                    anchor='red'
                    )
                )

        Example 2. Request division command active halfway through segment::

            >>> request = red_segment.request_division_command('Voice 1', multiplier=Multiplier(1, 2))

        ::

            >>> z(request)
            requesttools.CommandRequest(
                'divisions',
                'Voice 1',
                symbolictimetools.SymbolicOffset(
                    anchor='red',
                    multiplier=durationtools.Multiplier(1, 2)
                    )
                )

        Example 3. Request division command active at ``1/4`` 
        after start of measure ``8``::

            >>> timespan = red_segment.select_background_measures(8, 9)
            >>> offset = durationtools.Offset(1, 4)

        ::

            >>> request = red_segment.request_division_command('Voice 1', timespan=timespan, addendum=offset)

        ::

            >>> z(request)
            requesttools.CommandRequest(
                'divisions',
                'Voice 1',
                symbolictimetools.SymbolicOffset(
                    anchor=symbolictimetools.BackgroundMeasureSelector(
                        anchor='red',
                        start_identifier=8,
                        stop_identifier=9
                        ),
                    addendum=durationtools.Offset(1, 4)
                    )
                )

        Specify symbolic offset with `timespan`, `edge`, `multiplier`, `offset`.

        Postprocess command with any of `index`, `count`, `reverse`.

        Return command request.        
        '''
        timespan = timespan or self.specification_name
        symbolic_offset = symbolictimetools.SymbolicOffset(
            anchor=timespan, edge=edge, multiplier=multiplier, addendum=addendum)
        return requesttools.CommandRequest(
            'divisions', voice, symbolic_offset=symbolic_offset, reverse=reverse)

    def request_divisions(self, voice, anchor=None, time_relation=None, reverse=None):
        r'''Request segment divisions in `voice`::

            >>> request = red_segment.request_divisions('Voice 1')

        ::

            >>> z(request)
            requesttools.MaterialRequest(
                'divisions',
                'Voice 1',
                'red'
                )

        Return material request.        
        '''
        anchor = anchor or self.specification_name
        return requesttools.MaterialRequest(
            'divisions', voice, anchor, time_relation=time_relation, reverse=reverse)

    def request_naive_beats(self, voice, anchor=None, time_relation=None, reverse=None):
        r'''Request segment naive beats in `voice`::

            >>> request = red_segment.request_naive_beats('Voice 1')

        ::

            >>> z(request)
            requesttools.MaterialRequest(
                'naive_beats',
                'Voice 1',
                'red'
                )

        Return material request.        
        '''
        assert isinstance(voice, str)
        anchor = anchor or self.specification_name
        return requesttools.MaterialRequest(
            'naive_beats', voice, anchor, time_relation=time_relation, reverse=reverse)

    def request_rhythm(self, voice, anchor=None, time_relation=None, reverse=None):
        r'''Request segment rhythm in `voice`::

            >>> request = red_segment.request_rhythm('Voice 1')

        ::

            >>> z(request)
            requesttools.MaterialRequest(
                'rhythm',
                'Voice 1',
                'red'
                )

        Return rhythm request.        
        '''
        anchor = anchor or self.specification_name
        return requesttools.MaterialRequest(
            'rhythm', voice, anchor, 
            time_relation=time_relation, reverse=reverse)

    # TODO: replace 'timespan', 'edge', 'multiplier' keywords and with (symbolic) 'offset' keyword
    def request_rhythm_command(self, voice, 
        timespan=None, edge=None, multiplier=None, addendum=None, reverse=None):
        r'''Request segment rhythm command active at offset in `voice`.

        Example. Request rhythm command active at start of segment::

            >>> request = red_segment.request_rhythm_command('Voice 1')

        ::

            >>> z(request)
            requesttools.CommandRequest(
                'rhythm',
                'Voice 1',
                symbolictimetools.SymbolicOffset(
                    anchor='red'
                    )
                )

        Specify symbolic offset with segment-relative `edge`, `multiplier`, `offset`.

        Postprocess command with any of `index`, `count`, `reverse`.

        Return command request.        
        '''
        timespan = timespan or self.specification_name
        symbolic_offset = symbolictimetools.SymbolicOffset(
            anchor=timespan, edge=edge, multiplier=multiplier, addendum=addendum)
        return requesttools.CommandRequest(
            'rhythm', voice, symbolic_offset=symbolic_offset, reverse=reverse)

    # TODO: replace 'timespan', 'edge', 'multiplier' keywords with (symbolic) 'offset' keyword
    def request_time_signature_command(self, voice,
        timespan=None, edge=None, multiplier=None, addendum=None, reverse=None):
        r'''Request segment time signature command active at offset
        in `context`.

        Example. Request time signature command active at start of segment ``'red'``::

            >>> request = red_segment.request_time_signature_command('Voice 1')

        ::

            >>> z(request)
            requesttools.CommandRequest(
                'time_signatures',
                'Voice 1',
                symbolictimetools.SymbolicOffset(
                    anchor='red'
                    )
                )

        Specify symbolic offset with segment-relative `edge`, `multiplier`, `offset`.

        Postprocess command with any of `index`, `count`, `reverse`.

        Return command request.
        '''
        timespan = timespan or self.specification_name
        symbolic_offset = symbolictimetools.SymbolicOffset(
            anchor=timespan, edge=edge, multiplier=multiplier, addendum=addendum)
        return requesttools.CommandRequest(
            'time_signatures', voice, symbolic_offset=symbolic_offset, reverse=reverse)

    def request_time_signatures(self, voice, anchor=None, time_relation=None, reverse=None):
        r'''Request voice ``1`` time signatures that start during segment ``'red'``::

            >>> request = red_segment.request_time_signatures('Voice 1')

        ::

            >>> z(request)
            requesttools.MaterialRequest(
                'time_signatures',
                'Voice 1',
                'red'
                )

        Return material request.
        '''
        assert isinstance(voice, str)
        anchor = anchor or self.specification_name
        return requesttools.MaterialRequest(
            'time_signatures', voice, anchor, time_relation=time_relation, reverse=reverse)

    @abc.abstractmethod
    def select(self):
        pass
