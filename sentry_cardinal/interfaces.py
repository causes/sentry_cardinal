import sentry.interfaces
from sentry.web.helpers import render_to_string

class Stacktrace(sentry.interfaces.Stacktrace):
    score = 1000

    def get_hash(self):
            output = []
            for frame in self.frames:
                if frame.get('module'):
                    output.append(frame['module'])
                else:
                    output.append(frame['filename'])

                if frame.get('cleaned_function'):
                    output.append(frame['cleaned_function'])
                elif frame.get('function'):
                    output.append(frame['function'])
                else:
                    output.append(frame['lineno'])
            return output

    def to_html(self, event):
        frames = []
        for frame in self.frames:
            if frame.get('context_line'):
                context = sentry.interfaces.get_context(frame['lineno'], frame['context_line'], frame.get('pre_context'), frame.get('post_context'))
                start_lineno = context[0][0]
            else:
                context = []
                start_lineno = None

            context_vars = []
            if frame.get('vars'):
                context_vars = self._shorten(frame['vars'])
            else:
                context_vars = []

            frames.append({
                'abs_path': frame.get('abs_path'),
                'filename': frame['filename'],
                'function': frame.get('function'),
                'start_lineno': start_lineno,
                'lineno': frame.get('lineno'),
                'context_type': frame.get('context_type'),
                'context': context,
                'vars': context_vars,
            })

        return render_to_string('sentry_cardinal/partial/interfaces/stacktrace.html', {
            'event': event,
            'frames': frames,
            'stacktrace': self.get_traceback(event),
        })
