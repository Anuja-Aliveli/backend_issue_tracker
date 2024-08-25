# Projects list column 
PROJECT_COLUMNS_MAPPING = [
    {'label': 'Project ID',
     'fieldname': 'project_id',
     'fieldtype': 'link'},
    {'label': 'Project name',
     'fieldname': 'project_name',
     'fieldtype': 'string'},
    {'label': 'Project type',
     'fieldname': 'project_type',
     'fieldtype': 'string'},
    {'label': 'Project status',
     'fieldname': 'project_status',
     'fieldtype': 'status'},
    {'label': 'Created At',
     'fieldname': 'created_at',
     'fieldtype': 'dateTime'},
    {'label': 'Last Updated',
     'fieldname': 'updated_at',
     'fieldtype': 'dateTime'},
]

# Projects list action mapping
PROJECTS_ACTION_OPTIONS = [
    {
      'actId': 0,
      'label': 'Edit',
      'value': 'edit',
    },
    {
      'actId': 1,
      'label': 'View',
      'value': 'view',
    },
    {
      'actId': 2,
      'label': 'Close',
      'value': 'close',
    },
  ]
