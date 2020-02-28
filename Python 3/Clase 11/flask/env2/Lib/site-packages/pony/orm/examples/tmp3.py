
db.bind(provider='postgres', user=args.username, password=args.password, host=args.host ,port=args.port, database='image_labeling')

db.generate_mapping(create_tables=False)

with db_session:
    unit = WorkUnit[437]
    assignedworkitems = list(select(item for item in Assignedworkitem if item.workunitid.unitid == unit.unitid))

    for img in assignedworkitems:
        assignedworkitems += list(select(
            item for item in Assignedworkitem
            if item.workitemid == img.workitemid
               and str(item.workunitid.associatedlabels) == str(img.workunitid.associatedlabels)
               and item not in assignedworkitems
        ))
    print(assignedworkitems)

    unit.updatedate=datetime.now()