import pathlib
import os

publishPath = "//var//lib//jenkins//workspace//zzzz_upload_test//external"
try:
  print(f'Current Working dir path: {os.getcwd()}')
  print(f'Publish path: {publishPath}')
  os.chdir(publishPath)
  print(f'Current Working dir path: {os.getcwd()}')
except Exception as error:
  print(f'Current Working dir path: {os.getcwd()}')
  print(f'Error occured: {error}')
