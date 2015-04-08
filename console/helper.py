#encoding: utf-8

# Sys modules
import json
from django.http import HttpResponse

# User define modules
from base import Base

def render_to_json_response(context, **response_kwargs):
	data = json.dumps(context)
	response_kwargs['content_type'] = 'application/json'
	return HttpResponse(data, **response_kwargs)


class Runner(Base):

	@staticmethod
	def run(job_id):
		pass
