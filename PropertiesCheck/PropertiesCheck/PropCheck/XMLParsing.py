import os
import csv
import xml.etree.ElementTree as et


def parse(FILE_NAME):
    def write(sessions, wm):
        with open(output_file, wm, newline='') as csvfile:
            csvwriter = csv.writer(csvfile)

            for session in sessions:
                rows = []
                d = dict()
                session_name = session.get('NAME')
                session_reusable = session.get('REUSABLE')
                attributes = session.findall('CONFIGREFERENCE/ATTRIBUTE')

                for i in attributes:
                    if i.attrib['NAME'] == 'Stop on errors' or i.attrib['NAME'] == 'Override tracing':
                        d[i.attrib['NAME']] = i.attrib['VALUE']
                if 'Stop on errors' not in d:
                    d['Stop on errors'] = Default_SOE_Value
                if 'Override tracing' not in d:
                    d['Override tracing'] = Default_OT_Value
                csvwriter.writerow([session_name, session_reusable, d['Stop on errors'], d['Override tracing']])

    file_name = FILE_NAME
    full_file = os.path.abspath(file_name)
    output = 'C:/Users/arunatesan/PycharmProjects/PropertiesCheck/PropertiesCheck/XMLfiles/output/session_properties.csv'
    output_file = os.path.abspath(output)

    tree = et.parse(full_file)
    root = tree.getroot()
    workflows = root.findall('REPOSITORY/FOLDER/WORKFLOW')
    worklets = root.findall('REPOSITORY/FOLDER/WORKLET')
    sessions = root.findall('REPOSITORY/FOLDER/SESSION')
    config = root.findall('REPOSITORY/FOLDER/CONFIG/ATTRIBUTE')

    for i in config:
        if i.attrib['NAME'] == 'Stop on errors':
            DSOE = i.attrib['NAME']
            Default_SOE_Value = i.attrib['VALUE']
        if i.attrib['NAME'] == 'Override tracing':
            DOT = i.attrib['NAME']
            Default_OT_Value = i.attrib['VALUE']

    fields = ['SESSION_NAME', 'IS_REUSABLE', 'STOP_ON_ERRORS', 'OVERRIDE_TRACING']
    properties = ['Stop on errors', 'Override tracing']

    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

    write(sessions, 'a')

    for workflow in workflows:
        sessions = workflow.findall('SESSION')
        if workflow.attrib['NAME'] != 'WF_SAFETY_FF_TO_LND_LOAD' and sessions:
            write(sessions, 'a')

    for worklet in worklets:
        sessions = worklet.findall('SESSION')
        if sessions:
            write(sessions, 'a')

    return output

