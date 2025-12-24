<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html> 
<body>
  <h2>Airline Recorded</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th style="text-align:left">Airline</th>
      <th style="text-align:left">Destination</th>
    </tr>
    <xsl:for-each select="airlines/airline">
    <tr>
      <td><xsl:value-of select="name"/></td>
      <td>
          <xsl:value-of select="destination/from"/>
          <xsl:text> to </xsl:text>
          <xsl:value-of select="destination/to"/>
       </td>
    </tr>
    </xsl:for-each>
  </table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>

