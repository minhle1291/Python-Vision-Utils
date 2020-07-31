# open image dataset (oid) native notation [xmin, xmax, ymin, ymax] with each value as [0, 1] ratios
# darknet native notation [xcenter, ycenter, width, height] with each value as ratios [0, 1]

def darknet_to_oid(darknet_xc, darknet_yc, darknet_xw, darknet_yw):
  oid_xmin = darknet_xc - darknet_xw/2
  oid_xmax = darknet_xc + darknet_xw/2
  oid_ymin = darknet_yc - darknet_yw/2
  oid_ymax = darknet_yc + darknet_yw/2
  return oid_xmin, oid_xmax, oid_ymin, oid_ymax

def darknet_to_coord(darknet_xc, darknet_yc, darknet_xw, darknet_yw, img_width, img_height, zeroD=True):
  coord_darknet_xmin = darknet_xc - darknet_xw/2
  coord_darknet_xmax = darknet_xc + darknet_xw/2
  coord_darknet_ymin = darknet_yc - darknet_yw/2
  coord_darknet_ymax = darknet_yc + darknet_yw/2
  x0 = coord_darknet_xmin*img_width
  x1 = coord_darknet_xmax*img_width
  y0 = coord_darknet_ymin*img_height
  y1 = coord_darknet_ymax*img_height
  if zeroD: return x0, x1, y0, y1
  coord_darknet_x0y0 = [coord_darknet_xmin*img_width, coord_darknet_ymin*img_height]
  coord_darknet_x1y0 = [coord_darknet_xmax*img_width, coord_darknet_ymin*img_height]
  coord_darknet_x0y1 = [coord_darknet_xmin*img_width, coord_darknet_ymax*img_height]
  coord_darknet_x1y1 = [coord_darknet_xmax*img_width, coord_darknet_ymax*img_height]
  return coord_darknet_x0y0, coord_darknet_x1y0, coord_darknet_x0y1, coord_darknet_x1y1

def oid_to_darknet(oid_xmin, oid_xmax, oid_ymin, oid_ymax):
  darknet_xc = (oid_xmin + oid_xmax)/2
  darknet_yc = (oid_ymin + oid_ymax)/2
  darknet_xw = abs(oid_xmax - oid_xmin)
  darknet_yw = abs(oid_ymax - oid_ymin)
  return darknet_xc, darknet_yc, darknet_xw, darknet_yw

def oid_to_coord(oid_xmin, oid_xmax, oid_ymin, oid_ymax, img_width, img_height, zeroD=True):
  x0 = oid_xmin*img_width
  x1 = oid_xmax*img_width
  y0 = oid_ymin*img_height
  y1 = oid_ymax*img_height
  if zeroD: return x0, x1, y0, y1
  coord_oid_x0y0 = [x0, y0]
  coord_oid_x1y0 = [x1, y0]
  coord_oid_x0y1 = [x0, y1]
  coord_oid_x1y1 = [x1, y1]
  return coord_oid_x0y0, coord_oid_x1y0, coord_oid_x0y1, coord_oid_x1y1
