package singlylinkedlists

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestSinglyLinkedList_GetFirstValue(t *testing.T) {
	list := New[string]()
	_, err := list.GetFirstValue()
	assert.NotNil(t, err)
	list.Add("abc")

	value, err := list.GetFirstValue()
	assert.Nil(t, err)
	assert.Equal(t, "abc", value)

	list.Add("def")
	value, err = list.GetFirstValue()
	assert.Nil(t, err)
	assert.Equal(t, "abc", value)

	list.InsertAt(0, "111")
	value, err = list.GetFirstValue()
	assert.Nil(t, err)
	assert.Equal(t, "111", value)

}

func TestSinglyLinkedList_GetLastValue(t *testing.T) {
	list := New[string]()

	_, err := list.GetLastValue()
	assert.NotNil(t, err)

	list.Add("abc")
	value, err := list.GetLastValue()
	assert.Nil(t, err)
	assert.Equal(t, "abc", value)

	list.Add("def")
	value, err = list.GetLastValue()
	assert.Nil(t, err)
	assert.Equal(t, "def", value)

	list.InsertAt(2, "222")
	value, err = list.GetLastValue()
	assert.Nil(t, err)
	assert.Equal(t, "222", value)

}
