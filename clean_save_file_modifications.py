
import sublime
import sublime_plugin


class CleanSaveFileModificationsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view     = self.view
        settings = view.settings()

        self.disableModifers( settings )

        view.window().run_command( "save" )
        sublime.set_timeout_async( lambda: self.enableModifers( settings ), 1000 )

    def disableModifers(self, settings):
        self.ensure_newline_at_eof_on_save     = settings.get( 'ensure_newline_at_eof_on_save', False )
        self.trim_trailing_white_space_on_save = settings.get( 'trim_trailing_white_space_on_save', False )

        settings.set( 'ensure_newline_at_eof_on_save', False )
        settings.set( 'trim_trailing_white_space_on_save', False )

    def enableModifers(self, settings):
        settings.set( 'trim_trailing_white_space_on_save', self.trim_trailing_white_space_on_save )
        settings.set( 'ensure_newline_at_eof_on_save', self.ensure_newline_at_eof_on_save )

